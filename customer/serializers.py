from rest_framework import serializers 
from .models import Trending

class TrendingSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta:
        model = Trending
        fields = ['date','heading', 'category', 'pic']
