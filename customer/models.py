from django.db import models
from django.contrib.auth.models import User




# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics/', null='true', blank= 'true')
    phone = models.CharField(max_length=11)
    hobbies = models.CharField(max_length=300, default='')
    mail = models.EmailField(max_length=50)
    

    

    


    

