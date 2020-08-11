from django import forms
from .models import Profile, Trending
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    image = forms.ImageField(required=False, widget=forms.FileInput)
    class Meta:
        model = Profile
        fields = ['image','phone','hobbies','quotes']




class TrendingForm(forms.ModelForm): 
    pic = forms.ImageField(required=False, widget=forms.FileInput)
    class Meta:  
        model = Trending  
        fields = ['category','heading','pic','blog']
   


class PUForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__" 