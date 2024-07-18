from data_fetcher_and_parser import DataParser as d

'''
This module imports the "DataParser" class from
"data_fetcher_and_parser.py" and uses it to create subclasses,
one which displays a basic weather forecast (without humidity)
and one which displays a detailed one.
'''

# Class to provide a basic weather forecast for a city

class WeatherDisplayer(d):
    def __init__(self, city):
        super().__init__(city)
        self.detailed = False
        self.parsed_data = self.parse_weather_data(self.detailed)

    def display_weather(self):
        return self.parsed_data
    
# Class to provide a detailed weather forecast for a city

class DetailedWeatherDisplayer(d):
    def __init__(self, city):
        super().__init__(city)
        self.detailed = True
        self.parsed_data = self.parse_weather_data(self.detailed)
    
    def display_detailed_weather(self):
        return self.parsed_data