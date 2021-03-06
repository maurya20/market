from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.db import models
from .forms import ProfileForm, TrendingForm
from django.http import HttpResponse
from customer.models import Profile, Trending
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.auth.decorators import user_passes_test

from rest_framework import viewsets
from .serializers import TrendingSerializer, UserSerializer, ProfileSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


# from django.contrib.auth import get_user_model
# User = get_user_model()
from rest_framework import generics


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class TrendingViewSet(viewsets.ModelViewSet):
    queryset = Trending.objects.all().filter().order_by('-id')
    serializer_class = TrendingSerializer


class ProfileDetail(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


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


@user_passes_test(lambda user: not user.username, login_url='/home', redirect_field_name=None)
def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User = auth.authenticate(username=username, password=password)
        if User is not None:
            auth.login(request, User)
            return redirect('home')
        else:
            messages.info(request, 'Invalid credentials')
            return render(request, 'userlogin.html')
    else:
        return render(request, 'userlogin.html')


def logout(request):
    auth.logout(request)
    return redirect('userlogin')


@login_required
def myblog(request):
    myblog = Trending.objects.filter(user_id=request.user.id)

    return render(request, 'myblog.html', {'myblog':myblog})


@login_required
def Profile(request):
    return render(request, 'profile.html')



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
 




def home(request):
    blg = Trending.objects.all().filter().order_by('-id')
    context = {
             'blg':blg,
            
             
    }
    return render(request, 'home.html', context)


def blog(request, id):
    prof = Trending.objects.get(id=id)
    
    context = {
             
             'prof':prof,
             
             
            }
    return render(request, 'blog.html', context)


def tb(request, user_id):
    total = Trending.objects.filter(user_id=user_id)
    author = User.objects.get(id=user_id)
    context = {
   
    'total':total,
    'author':author,
    
    }
    return render(request, 'tb.html', context)




@login_required
@transaction.atomic
def create(request):
    form = TrendingForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            article = form.save(commit=False) 
            article.user = request.user # you can check here whether user is related any author
            article.author = request.user
            article.save()
            
        return redirect('home')
    else:
        context = {'form': form }
        return render(request, 'create.html', context) 




def category(request, category):
    cat = Trending.objects.filter(category=category)
    cat_name = category
    context = {
   
    'cat':cat,
    'cat_name':cat_name,
    }
    return render(request, 'category.html', context)





    


