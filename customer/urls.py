from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from customer import views
from django.contrib import admin  
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.userlogin, name='userlogin'),
    path('home', views.home, name='home'),
    path('tb/<str:user_id>',views.tb, name='tb'),
    path('register', views.register, name='register'),
    path('userlogin', views.userlogin, name='userlogin'),
    path('profile', views.Profile, name='profile'),
    path('logout', views.logout, name='logout'),
    path('edit', views.edit, name='edit'),
    path('create',views.create, name='create'),
    path('category/<str:category>',views.category, name='category'),
    path('blog/<int:id>',views.blog, name='blog'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"),name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="reset_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="reset_confirm.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="reset_done.html"), name="password_reset_complete"),



]
    
    



