import requests

API_KEY = "bc3fd40d5214b7845ca106ce2b512c97"
city = input("Enter city name: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Temperature:", data['main']['temp'], "°C")
    print("Weather:", data['weather'][0]['description'])
    print("Humidity:", data['main']['humidity'], "%")
else:
    print("City not found.")
