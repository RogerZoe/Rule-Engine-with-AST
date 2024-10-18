import requests
import time
import pandas as pd

API_KEY = 'bd5e378503939ddaee76f12ad7a97608'
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
INTERVAL = 300  # 5 minutes

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={'Mumbai'}&appid={'bd5e378503939ddaee76f12ad7a97608'}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'city': city,
            'temp': kelvin_to_celsius(data['main']['temp']),
            'feels_like': kelvin_to_celsius(data['main']['feels_like']),
            'main': data['weather'][0]['main'],
            'timestamp': data['dt']
        }
    return None

def main():
    weather_data = []
    while True:
        for city in CITIES:
            data = get_weather_data(city)
            if data:
                weather_data.append(data)
        time.sleep(INTERVAL)
        if len(weather_data) > 10:  # Save to DB or process after collecting enough data
            df = pd.DataFrame(weather_data)
            print(df)
            # Reset after processing or persist to DB
            weather_data = []

if __name__ == "__main__":
    main()
