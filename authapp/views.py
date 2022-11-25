from urllib import response
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password =  request.POST['password']
        user = authenticate(
    		    request, 
    		    username=username, 
    		    password=password
        )

        if user is None:
            return HttpResponse("Invalid credentials.")
        
        login(request, user)
        return redirect('/')

    else:
        form = UserForm()
        return render(request, 'authapp/sign-in.html', {'form':form})


def signout(request):

    logout(request)
    return redirect('/')


def signup(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
        #email = request.POST['email']
        #password = request.POST['password']
        #username = request.POST['username']
            newuser = form.save(commit=False)
            try:
                newuser.save()
            except:
                return HttpResponse("Something went wron!")
        
    else:
        form = UserRegistrationForm()
    return render(request, 'authapp/sign-up.html', {'form':form})
