from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('register', views.register, name='register'),
    path('userlogin', views.userlogin, name='userlogin'),
    path('profile', views.Profile, name='profile'),
    path('logout', views.logout, name='logout'),
    path('test', views.test, name='test'),
    path('edit', views.edit, name='edit')
    
]
