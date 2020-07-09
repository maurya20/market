from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User, auth
from . models import Profile
from django.db import models
from .forms import ProfileForm
 


# Create your views here.
def home(request): 
    return render(request, 'home.html')

def test(request): 
    return render(request, 'test.html')



def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'This username has taken by other user')
                return render(request, 'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'This email has  already registerd ')
                return render(request, 'register.html')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, password=password1, email=email,
                                              last_name=last_name)
                user.save()
                
                messages.info(request, 'A new user created sucessfully')
                return redirect('userlogin')

        else:
            messages.info(request, 'Password not matching')
            return redirect('register')
    else:
        return render(request, 'register.html')


def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User = auth.authenticate(username=username, password=password)
        if User is not None:
            auth.login(request, User)
            messages.info(request, 'Login Successful')
            return render(request, 'home.html')


        else:
            messages.info(request, 'Invalid credentials')
            return redirect('userlogin')
    else:
        return render(request, 'userlogin.html')


def Profile(request):
    return render(request, 'profile.html')

def logout(request):
    auth.logout(request)
    return redirect('userlogin')


def edit(request):
    form = ProfileForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            Profile = form.save()
        return render(request, 'profile.html') 
    else:
        context = {'form': form }
        return render(request, 'edit.html', context)
 
    


