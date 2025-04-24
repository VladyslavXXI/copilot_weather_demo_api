from django.urls import reverse
from rest_framework.test import APIClient
from .models import City

class EgyptWeatherEndpointTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Ensure Egyptian cities exist
        for city in ["Cairo", "Alexandria", "Giza"]:
            City.objects.get_or_create(name=city)

    def test_egypt_weather_endpoint(self):
        url = reverse('egypt-weather')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        for city in ["Cairo", "Alexandria", "Giza"]:
            self.assertIn(city, data)
            # Should contain either weather data or an error key
            self.assertTrue('location' in data[city] or 'error' in data[city])
