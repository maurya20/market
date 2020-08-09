from django import forms
from .models import Profile, Trending


class ProfileForm(forms.ModelForm):
    image = forms.ImageField(required=False, widget=forms.FileInput)
    class Meta:
        model = Profile
        fields = ['image','phone','hobbies','quotes']




class TrendingForm(forms.ModelForm):  
    class Meta:  
        model = Trending  
        fields = "__all__"  


class PUForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','user']