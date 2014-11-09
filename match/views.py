from django.shortcuts import render, redirect, HttpResponse
#from django.contrib.auth.forms import UserCreateForm
from forms import UserCreateForm, InterestForm, DescriptionForm, FindFlightForm, SeatNumberForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from models import AirlineUser, Interest, Flight, PersonOnFlight
from GetFlightInfo import *
from GetHotelData import *
import json


def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            username = form.clean_username()
            password = form.clean_password2()
            u = form.save()
            p = AirlineUser(user=u)
            p.save()
            user = authenticate(username=username, password=password)
            login(request,user)
            #return render(request,'created_file.html')
            return redirect('match.views.success')
    else:
        form = UserCreateForm()
        #context = {"form":form}
        context = {}
        context['form'] = form
        return render(request, 'register.html',context)

def add_interests(request):
    #user = .AirlineUser
    current_user = request.user
    print(current_user.username)
    user = AirlineUser.objects.get(user__pk__exact=current_user.pk)
    if request.method=="POST":
        interest_form = InterestForm(request.POST)
        if interest_form.is_valid():
            text = request.POST['interest']
            L = Interest.objects.filter(name__iexact=text)
            if len(L)<1:
                interest_object = Interest(name=text)
                interest_object.save()
            else:
                interest_object = L[0]
            user.interests.add(interest_object)
        return redirect('match.views.profile')

    else:
        list_of_interests = user.interests.all()
        form = InterestForm()
        context = {"form":form, "interests":list_of_interests}
        return render(request, 'interests.html',context)

def create_new(request):
    return render(request,'createnew.html')

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            return redirect('match.views.index')
        else:
            return HttpResponse("WRONG")
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

def success(request):
    if request.user.is_authenticated():
        return render(request, 'success.html')
    else:
        return HttpResponse("idk")

def profile(request):
    current_user = request.user
    user = AirlineUser.objects.get(user__pk__exact=current_user.pk)
    list_of_interests = user.interests.all()
    travels = PersonOnFlight.objects.filter(person=user)
    flights = []
    for instance in travels:
        flights.append(instance.flight)
    context={}
    context['interest_form']=InterestForm()
    context['description_form']=DescriptionForm()
    context['interests']=list_of_interests
    context['flights']=flights

    return render(request, 'profile.html', context)

def find_flight(request):
    if request.method == "POST":
        form = FindFlightForm(request.POST)
        if form.is_valid():

            airline = form.cleaned_data['airline']
            origin = form.cleaned_data['origin']
            destination = form.cleaned_data['destination']
            date = form.cleaned_data['depart_date']
            date = date.strftime("%Y-%m-%d")
            list_of_flights = getFlights(date,origin,destination,airline)
            flight_json = []
            for flight in list_of_flights:
                d = {}
                d['number'] = flight.flightNumber
                d['origin'] = origin
                d['destination'] = destination
                d['departure'] = date
                flight_json.append(d)
            request.session["flight"]= json.dumps(flight_json)
            print request.session['flight']
            context = {}
            context['flights'] = list(enumerate(list_of_flights))
            return render(request,'choose_your_flight.html',context)
    else:
        form = FindFlightForm()
        context = {}
        context['form']=form
        return render(request, 'find_flight.html',context)

def flight_page(request,flight_number):
    flight = Flight.objects.get(pk=flight_number)
    context = {}
    context['id']=flight_number
    return render(request,'flight_main.html',context)

def addFlight(request):
    if request.method == "POST":
        current_user = request.user
        user = AirlineUser.objects.get(user__pk__exact=current_user.pk)
        flight_json= json.loads(request.session['flight'])
        index = int(request.POST['flight'])
        flight = flight_json[index]
        try:
            flights = Flight.objects.get(number=flight['number'])
            flight_model= flights
        except Flight.DoesNotExist:
            flight_model = Flight(number = flight['number'], destination=flight['destination'],origin = flight['origin'])
            flight_model.save()

        try:
            passengers = PersonOnFlight.objects.get(flight=flight_model,person=user)
            passenger=passengers[0]
        except PersonOnFlight.DoesNotExist:
            passenger = PersonOnFlight(person = user, flight=flight_model)
            passenger.save()

        return redirect('match.views.profile')
        #return HttpResponse("Yay")


def flight_profiles(request,flight_number):
    flight = Flight.objects.get(pk=flight_number)
    people = PersonOnFlight.objects.filter(flight__pk=flight_number)
    people_interests = []
    for person in people:
        people_interests.append((person,person.get_interests()))

    context = {}
    context['people_interests']=people_interests
    context['passengers']=people
    context['flight']=flight
    context['form']= SeatNumberForm()
    return render(request,'flight_users.html',context)

def friend_profile(request,friend_id):
    friend = PersonOnFlight.objects.get(pk=friend_id)
    flight = Flight.objects.get(persononflight__pk=friend_id)
    print flight.number
    interests = friend.get_interests()
    context = {}
    context['interests']=interests
    context['friend']=friend
    context['flight']=flight
    return render(request,'friend_profile.html',context)


def choose_seat(request,flight_number):
    current_user = request.user
    user = AirlineUser.objects.get(user__pk__exact=current_user.pk)
    flight = Flight.objects.get(pk=flight_number)
    person = PersonOnFlight.objects.get(person = user, flight__pk=flight_number)
    if request.method =="POST":
        seat = SeatNumberForm(request.POST)
        if seat.is_valid():
            person.seat_number=None

def select_hotel(request,flight_number):
    if request.method=="POST":
        hotels = request.session["hotels"]
        current_user = request.user


        user = AirlineUser.objects.get(user__pk__exact=current_user.pk)
        hotel_json= json.loads(request.session['hotels'])
        index = int(request.POST['hotel'])
        flight = hotel_json[index]
        try:
            flights = Flight.objects.get(number=flight['number'])
            flight_model= flights
        except Flight.DoesNotExist:
            flight_model = Flight(number = flight['number'], destination=flight['destination'],origin = flight['origin'])
            flight_model.save()

        try:
            passengers = PersonOnFlight.objects.get(flight=flight_model,person=user)
            passenger=passengers[0]
        except PersonOnFlight.DoesNotExist:
            passenger = PersonOnFlight(person = user, flight=flight_model)
            passenger.save()

        return redirect('match.views.profile')


    else:
        radius = 25 #km
        flight = Flight.objects.get(pk=flight_number)
        city = flight.origin
        hotels = hotelsNearAirport(city, radius)
        hotel_temp = []
        for hotel in hotels:
            jsn = {}
            jsn['name']=hotel.name
            jsn['address']=hotel.address
            hotel_temp.append(jsn)
        hotels = hotel_temp
        request.session["hotels"]= json.dumps(hotels)
        context = {}
        context['hotels'] = list(enumerate(hotels))
        return render(request,'choose_your_flight.html',context)


def send(request, friend_id):
    friend = PersonOnFlight.objects.get(pk=friend_id)
    email = friend.person.user.email
