from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from datetime import datetime




# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null='True', blank= 'True')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics/', null='True', blank= 'True')
    phone = models.CharField(max_length=11, null='True')
    hobbies = models.CharField(max_length=300, null='True')
    quotes = models.CharField(max_length=150, null='True')
    



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



class Trending(models.Model):
    CATEGORY_CHOICES = (
        ("Science & Education", "Science & Education"),
        ("Travel", "Travel"),
        ("Gadgets", "Gadgets"),
        ("History", "History"),
        ("Politics", "Politics"),
        ("Farming", "Farming"),
        ("Sports", "Sports"),
        ("Other", "Other"))
    category = models.CharField(max_length=120, choices=CATEGORY_CHOICES,default='Other') 
    heading = models.CharField('Blog Heading', max_length=120, null=True)
    blog = models.TextField(blank=True, null=True)
    date = models.DateField(default=datetime.now, null=True)
    pic = models.ImageField(default='blg.jpg', upload_to='blog/', null='True', blank= 'True')
    author = models.CharField(max_length=120, null=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null='True', blank= 'True')
    



    

