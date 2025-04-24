import requests

API_URL = "http://127.0.0.1:8000/api/weather/"
params = {"city": "Lviv"}

response = requests.get(API_URL, params=params)
print("Status code:", response.status_code)
print("Response:", response.json())
