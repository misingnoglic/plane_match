from django.shortcuts import render
#from django.contrib.auth.forms import UserCreateForm
from forms import UserCreateForm
from django.contrib.auth.models import User
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'created_file.html')
    else:
        form = UserCreateForm()
        context = {"form":form}
        context = {}
        context['form'] = form
        return render(request, 'register.html',context)
