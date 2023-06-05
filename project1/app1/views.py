

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
import requests

# password for test user is Harry$$$***000
# Create your views here.
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("login") 
    return render(request, 'index.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("login")

def signup_user(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('psw')
        pass2=request.POST.get('psw-repeat')
        
        my_user= User.objects.create_user(uname,email,pass1)
        my_user.save()
        return HttpResponse("user is created")
    return render(request,'signup.html')

