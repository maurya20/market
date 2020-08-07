from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from customer import views
from django.contrib import admin  


urlpatterns = [
    path('', views.userlogin, name='userlogin'),
    path('home', views.home, name='home'),
    path('register', views.register, name='register'),
    path('userlogin', views.userlogin, name='userlogin'),
    path('profile', views.Profile, name='profile'),
    path('logout', views.logout, name='logout'),
    path('edit', views.edit, name='edit'),
    path('create',views.create, name='create'),
   
    
]


