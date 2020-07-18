from django import forms
from .models import Profile, Event


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"




class EventForm(forms.ModelForm):  
    class Meta:  
        model = Event  
        fields = "__all__"  


class PUForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','user']