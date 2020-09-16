from rest_framework import serializers, status
from .models import Trending, Profile
from django.contrib.auth.models import User, auth

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]



class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    class Meta:
        model = Profile
        fields = "__all__"


class TrendingSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    class Meta:
        model = Trending
        fields = ['id','blog','date','heading', 'category', 'pic','author','user']


