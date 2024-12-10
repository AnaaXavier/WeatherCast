import os
import sys
import requests
import json

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from PySide6.QtGui import QPixmap
from Model import convert_degrees

class Weather_API:
    """
    All requests are sent to the API, if the results obtained from JSON are found, it returns an icon and tuples.
    
    An API key to access information is required.
    
    Methods: get_icon(icon_code), get_and_send_data_from_api(city, country_code)
    
    Param: api_key
    Methods params: icon_code, city, country_code
    """
    
    def __init__(self, api_key):
        self.key = api_key
        self.base_endpoint = "api.openweathermap.org"
    
    def get_icon(self, icon_code):
        # if the icon_code is provided, it retrieves the corresponding image and returns it as a QPixmap
        if icon_code:
            icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
            response = requests.get(icon_url)
            if response.status_code == 200:
                pixmap = QPixmap()
                pixmap.loadFromData(response.content)
                return pixmap
            
        return None

    def get_and_send_data_from_api(self, city, country_code):
        try:
            url = f"https://{self.base_endpoint}/data/2.5/weather?q={city},{country_code}&appid={self.key}"
            response = requests.get(url)
            response.raise_for_status()

            data = response.json()
            
            weather_icon = data["weather"][0]["icon"]

            country = data["sys"]["country"]
            temperature = data["main"]["temp"]
            temperature_in_celsius = convert_degrees.kelvin_to_celsius(temperature)
            temp_min = data["main"]["temp_min"]
            temp_max = data["main"]["temp_max"]
            temp_min_in_celsius = convert_degrees.kelvin_to_celsius(temp_min)
            temp_max_in_celsius = convert_degrees.kelvin_to_celsius(temp_max)
            
            description = data["weather"][0]["description"]
            visibility = data["visibility"]
            humidity = data["main"]["humidity"]
            thermic_sensation = data["main"]["feels_like"]
            
            thermic_sensation_in_celsius = convert_degrees.kelvin_to_celsius(thermic_sensation)
            
            wind_speed = data["wind"]["speed"]
            
            # packs into a tuple
            return weather_icon, country, temperature_in_celsius, temp_min_in_celsius, temp_max_in_celsius, description, humidity, visibility, thermic_sensation_in_celsius, wind_speed
            
        except requests.exceptions.RequestException as e:
            print(f"Connection error occurred: {e}")
            return None
        
        except json.decoder.JSONDecodeError as e:
            print(f"Error parsing JSON data: {e}")
            return None
        
        except KeyError as e:
            print(f"Missing expected data in the API response: {e}")
            return None
        
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None
