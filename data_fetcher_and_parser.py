'''
This module contains classes to fetch and parse weather data.
It is imported into weather_displayer.py.
'''

# Class to fetch weather data

class WeatherDataFetcher:
    def __init__(self, city):
        self.city = city
        self.data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
        }

    def fetch_weather_data(self):
        print(f"Fetching weather data for {self.city}...")

        return self.data.get(self.city, {})

# Class to parse weather data

class DataParser(WeatherDataFetcher):
    def __init__(self, city):
        super().__init__(city)
        self.data = self.fetch_weather_data()

    def parse_weather_data(self, detailed):
        if not self.data:
            return f"Weather data not available for {self.city}."
        
        city = self.data["city"]
        temperature = self.data["temperature"]
        condition = self.data["condition"]
        humidity = self.data["humidity"]

        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"\
        if detailed else f"Weather in {city}: {temperature} degrees, {condition}"