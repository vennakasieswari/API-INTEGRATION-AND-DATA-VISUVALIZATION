import requests
cityName = input("Enter your city : ")

city_name = 'markapur'
API_key = '4a28b7c5aabeb144c7b6d1e6b265937c'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'


response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print('weatheris', data['weather'][0]['description'])
   
    print('Current Temperature is', data['main']['temp'])
    print('Current Temperature Feels like is', data['main']['feels_like'])
    print('Humidity is' , data['main']['humidity'])
    print("maximum Temperature ", data["main"]["temp_max"])
    print("minimum Temperature", data["main"]["temp_min"])
    