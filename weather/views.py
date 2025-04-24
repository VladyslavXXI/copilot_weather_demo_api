from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import City
from .serializers import CitySerializer, WeatherRequestSerializer
import requests
from django.conf import settings

WEATHER_API_KEY = "73f6bc9242f24f8d8bb135152252304"
WEATHER_API_URL = "http://api.weatherapi.com/v1/current.json"

class GetWeatherView(APIView):
    def get(self, request):
        city_name = request.query_params.get('city')
        if not city_name:
            return Response({"error": "City query parameter is required."}, status=status.HTTP_400_BAD_REQUEST)
        if not City.objects.filter(name__iexact=city_name).exists():
            return Response({"error": "Unsupported city."}, status=status.HTTP_400_BAD_REQUEST)
        params = {
            'key': WEATHER_API_KEY,
            'q': city_name
        }
        r = requests.get(WEATHER_API_URL, params=params)
        if r.status_code == 200:
            return Response(r.json())
        return Response({"error": "Failed to fetch weather."}, status=status.HTTP_502_BAD_GATEWAY)

class AddCityView(APIView):
    def post(self, request):
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            city, created = City.objects.get_or_create(name=serializer.validated_data['name'])
            if created:
                return Response({"message": "City added."}, status=status.HTTP_201_CREATED)
            return Response({"message": "City already exists."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RemoveCityView(APIView):
    def delete(self, request):
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            city_name = serializer.validated_data['name']
            deleted, _ = City.objects.filter(name__iexact=city_name).delete()
            if deleted:
                return Response({"message": "City removed."}, status=status.HTTP_200_OK)
            return Response({"error": "City not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SupportedCitiesView(APIView):
    def get(self, request):
        cities = City.objects.values_list('name', flat=True)
        return Response({"cities": list(cities)})

class EgyptWeatherView(APIView):
    def get(self, request):
        egyptian_cities = ["Cairo", "Alexandria", "Giza"]
        results = {}
        for city in egyptian_cities:
            if not City.objects.filter(name__iexact=city).exists():
                results[city] = {"error": "City not supported in DB."}
                continue
            params = {
                'key': WEATHER_API_KEY,
                'q': city
            }
            r = requests.get(WEATHER_API_URL, params=params)
            if r.status_code == 200:
                results[city] = r.json()
            else:
                results[city] = {"error": "Failed to fetch weather."}
        return Response(results)
