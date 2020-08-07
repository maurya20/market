from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver




# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics/', null='True', blank= 'True')
    phone = models.CharField(max_length=11, null='True')
    hobbies = models.CharField(max_length=300, null='True')
    quotes = models.CharField(max_length=150, null='True')
    blog = models.TextField(max_length=850, null='True')



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()









class Event(models.Model):  
    name = models.CharField('Event Name', max_length=120)
    venue = models.CharField(max_length=120)
    manager = models.CharField(max_length=60)
    description = models.TextField(blank=True)

    

    


    

