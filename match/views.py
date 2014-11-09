from django.shortcuts import render, redirect, HttpResponse
#from django.contrib.auth.forms import UserCreateForm
from forms import UserCreateForm, InterestForm, DescriptionForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from models import AirlineUser, Interest

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
    print user
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

    else:
        pass
    list_of_interests = user.interests.all()
    print(list_of_interests)

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
    context = {'interest_form':InterestForm(), 'description_form':DescriptionForm()}

    return render(request, 'profile.html', context)

'''def createnew(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            departFrom = form.clean_username()
            departTo = form.clean_password2()
            departDate = form.
            form.save()
            login(request,user)
            #return render(request,'created_file.html')
            return redirect('match.views.success')
    else:
        form = UserCreateForm()
        context = {"form":form}
        context = {}
        context['form'] = form
        return render(request, 'register.html',context)
'''