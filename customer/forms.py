from django import forms
from .models import Profile, Event


class ProfileForm(forms.ModelForm):
    image = forms.ImageField(required=False, widget=forms.FileInput)
    class Meta:
        model = Profile
        fields = ['image','phone','hobbies','quotes','blog']




class EventForm(forms.ModelForm):  
    class Meta:  
        model = Event  
        fields = "__all__"  


class PUForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','user']