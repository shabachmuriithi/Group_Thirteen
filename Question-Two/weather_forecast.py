class WeatherForecastApp:
    def __init__(self):
        self.cities = {}

    def add_city(self, city_name, temperature, humidity, wind_speed):
        self.cities[city_name] = {
            "temperature":temperature,
            "humidity":humidity,
            "wind_speed":wind_speed
        }
        return f"Added weather data for {city_name}: Temp = {temperature} degrees celcius, Humidity = {humidity}%, Wind = {wind_speed}km/h"

    def get_city_weather(self,city_name):
        info = self.cities.get(city_name)
        if info:
            print(f"{city_name} Weather =>Temp:{info['temperature']} degrees celcius, Humidity:{info['humidity']}%, Wind:{info['wind_speed']}km/h")
            return info
        else:
            print(f"No weather data found for {city_name}")
        
        