import requests

# API Key for test purposes. Already deactivated
API_KEY = "85a3afdc696d74fd74011926715a892b"
WEATHER_URL = f"https://api.openweathermap.org/data/2.5/weather?appid={API_KEY}"
# https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=85a3afdc696d74fd74011926715a892b
GEO_URL = f"https://api.openweathermap.org/geo/1.0/direct?appid={API_KEY}"


def get_geo_coordinates(city):
    request_url = f"{GEO_URL}&q={city}"
    response = requests.get(request_url)
    if response.status_code == 200:
        response_data = response.json()[0]
        return {"lat": response_data["lat"], "lon": response_data["lon"]}
    else:
        print(response.json())
        print("An error occurred.")


def get_weather(city, coordinates):
    # For newer versions, latitude and longitude are required params
    lat, lon = coordinates["lat"], coordinates["lon"]
    request_url = f"{WEATHER_URL}&q={city}&lat={lat}&lon={lon}"
    response = requests.get(request_url)
    if response.status_code == 200:
        return response.json()
    else:
        print(response.json())
        print("An error occurred.")


city = input("Enter a city name: ")
coordinates = get_geo_coordinates(city)
weather = get_weather(city, coordinates)
print(weather)
