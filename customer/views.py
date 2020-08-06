from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.db import models
from .forms import ProfileForm, EventForm, PUForm
from django.http import HttpResponse
from customer.models import Profile, Event
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db import transaction


# Create your views here.
def home(request):
    return render(request, 'home.html')



 
def crud(request):  
    if request.method == "POST":  
        form = EventForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/profile')  
            except:  
                pass  
    else:  
        form = EventForm()  
    return render(request,'profile.html', {'form':form}) 


def destroy(request):  
    prof = Event.objects.get()  
    prof.delete()  
    return redirect("/edit") 



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
    if request.method == 'POST':
        p_form = PUForm(request.POST, request.FILES)
        if p_form.is_valid():
            p_form.save()
        return redirect('profile')
    else:
        p_form = PUForm()
        context = {'p_form': p_form }
        return render(request, 'profile.html', context)

def logout(request):
    auth.logout(request)
    return redirect('userlogin')

@login_required
@transaction.atomic
def edit(request):
    form = ProfileForm(request.POST or None, request.FILES or None, instance=request.user.profile)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('profile')
    else:
        context = {'form': form }
        return render(request, 'edit.html', context)
 
    


