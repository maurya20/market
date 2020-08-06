from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver




# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics/', null='True', blank= 'True')
    phone = models.CharField(max_length=11)
    hobbies = models.CharField(max_length=300, default='')
    quotes = models.TextField(max_length=350)






class Event(models.Model):  
    name = models.CharField('Event Name', max_length=120)
    venue = models.CharField(max_length=120)
    manager = models.CharField(max_length=60)
    description = models.TextField(blank=True)

    

    


    

