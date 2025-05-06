from rest_framework import serializers
from .models import Review,WatchList

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Review
        fields= "__all__"   

class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True,read_only=True)
    class Meta:
        model=WatchList
        fields= "__all__"
