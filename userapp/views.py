
from django.shortcuts import render, redirect  
from django.contrib.auth import login,logout, authenticate
from django.http import HttpResponse
from .forms import DataForm
from .models import details
from django.contrib.auth.models import User
from django.db import IntegrityError
# Create your views here.

def home(request):
    return render(request,"home.html")


def register(request):
   
     if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        
        # Create the user object
        try:
            user = User.objects.create_user(username=username, password=password, email=email)
            return redirect('/accounts/login')
        except IntegrityError as e:
            error_message = 'Username already exists. Please choose a different username.'
            return render(request, 'register.html', {'error': error_message})
        
     
    
     return render(request, 'register.html')

def loginUser(request):
   
    if request.method == 'POST':
         username = request.POST.get('name')
         password = request.POST.get('password')

         user=authenticate(request,username = username,password = password)
         if user is not None:
           login(request, user)
           return redirect('/home')
        
         else:
            error = ('Invalid username or password')
            return render(request,'login.html',{'error': error})
        
    return render(request, 'login.html')
            # messages.success(request, f'Your account has been created. You can log in now!')
     


def logoutUser(request):
    logout(request)
    return redirect('/accounts/login')

