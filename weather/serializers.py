from rest_framework import serializers
from .models import City

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name']

class WeatherRequestSerializer(serializers.Serializer):
    city = serializers.CharField(max_length=100)
