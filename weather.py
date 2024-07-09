from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city='Castro Valley'):
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'
    
    weather_data = requests.get(request_url).json()
    
    return weather_data

if __name__ == "__main__":
    print("\n*** Get Weather Condiction ***\n")
    
    city = input("\nEnter a city name: ")
    
    if not bool(city.strip()):
        city = 'Castro Valley'
        
    weather_data = get_current_weather(city)
    
    if weather_data['cod'] != 200:
        weather_data = get_current_weather()
        
        
    print("\n")
    
    pprint(weather_data)
