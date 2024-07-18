from weather_displayer import WeatherDisplayer as w, DetailedWeatherDisplayer as dw

'''
This module contains the user interface and "main()" function for the application.
It imports the "WeatherDisplayer" and "DetailedWeatherDisplayer" classes from
"weather_displayer.py" and incorporates them into the "UserInterface" class.
'''

# Task 1: Identifying and Creating Classes

class UserInterface():
    def display_user_interface():
        while True:
            city = input("Enter the city to get the weather forecast or 'exit' to quit: ")

            if city.lower() == 'exit':
                break

            detailed = input("Do you want a detailed forecast? (yes/no): ").lower()

            forecast = dw(city).display_detailed_weather() if detailed == "yes"\
            else w(city).display_weather()

            print(forecast)

def main():
    UserInterface.display_user_interface()

if __name__ == "__main__":
    main()