from django.shortcuts import render, redirect, HttpResponse
#from django.contrib.auth.forms import UserCreateForm
from forms import UserCreateForm, InterestForm, DescriptionForm, FindFlightForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from models import AirlineUser, Interest
from GetFlightInfo import *

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
        print 1
        interest_form = InterestForm(request.POST)
        if interest_form.is_valid():
            print 2
            text = request.POST['interest']
            L = Interest.objects.filter(name__iexact=text)
            if len(L)<1:
                print 3
                interest_object = Interest(name=text)
                interest_object.save()
            else:
                print 4
                interest_object = L[0]
            user.interests.add(interest_object)
            print 5
        print 6
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
    context = {'interest_form':InterestForm(), 'description_form':DescriptionForm(),
               'interests':list_of_interests}

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
            request.list_of_flights= list_of_flights
            context = {}
            context['flights'] = list(enumerate(list_of_flights))
            return render(request,'choose_your_flight.html',context)
    else:
        form = FindFlightForm()
        context = {}
        context['form']=form
        return render(request, 'find_flight.html',context)

def addFlight(request):
    if request.method == "POST":
        list_of_flights= request.list_of_flights
        index = request.airline
        flight = list_of_flights[index]
