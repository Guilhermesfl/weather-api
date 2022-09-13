import requests

# API Key for test purposes. Already deactivated
API_KEY = "85a3afdc696d74fd74011926715a892b"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")

request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
print(request_url)
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(response.json())
    print("An error occurred.")
