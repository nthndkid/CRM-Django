from django.shortcuts import render, redirect
# import auth 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    if request.method == "POST":
        username = request.POST['username']
        passwword = request.POST['password']
        # authenticate
        user = authenticate(request, username=username, passwword=passwword)
        # if valid 
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        else:
            messages.error(request, "Invalid Username or Password")
            return redirect('home')
    else:
        return render(request, 'home.html')

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out..")
    return redirect('home')

def register_user(request):
    return render(request, 'register.html')

