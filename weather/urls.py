from django.urls import path
from .views import GetWeatherView, AddCityView, RemoveCityView, SupportedCitiesView

urlpatterns = [
    path('weather/', GetWeatherView.as_view(), name='get-weather'),
    path('add-city/', AddCityView.as_view(), name='add-city'),
    path('remove-city/', RemoveCityView.as_view(), name='remove-city'),
    path('supported-cities/', SupportedCitiesView.as_view(), name='supported-cities'),
]
