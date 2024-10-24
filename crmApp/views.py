from django.shortcuts import render, redirect
# import auth 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.
def home(request):
    records = Record.objects.all()

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
        context = {'records':records}
        return render(request, 'home.html', context)

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out..")
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # authenticate and login
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered!")
            return redirect('home')
    else:
        form = SignUpForm()
        context = {'form':form}
        return render(request, 'register.html', context)
    context = {'form':form}
    return render(request, 'register.html', context)

def customer_record(request, pk):
    if request.user.is_authenticated:
        # display records
        customer_record = Record.objects.get(id=pk)
        context = {'customer_record':customer_record}
        return render(request, 'record.html', context)
    else:
        messages.info(request, "You Must Be Logged In To Access That Page!")
        return redirect(home)
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        record.delete()
        messages.success(request, "Record Deleted Successfully!")
        return redirect('home')
    else:
        messages.info(request, "You Must Be Logged In To Access That Page!")
        return redirect('home')
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "New Record Added!")
                return redirect('home')
        context = {'form':form}
        return render(request, 'add_record.html', context)
    else:
        messages.info(request, "You Must Be Logged In To Access That Page!")
        return redirect('home')

def update_record(request, pk):
    if request.user.is_authenticated:
        existing_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=existing_record)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Record Updated Successfully!")
                return redirect('home')
        context = {'form':form}
        return render(request, 'update_record.html', context)
    else:
        messages.info(request, "You Must Be Logged In To Access That Page!")
        return redirect('home')
        
