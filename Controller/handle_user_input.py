import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from View import customized_message_box

def handle_missing_inputs(city, country_code):
    """
    Verifies if there's any empty inputs.
    
    Args:
        city (str): city's name given by user.
        country_code(str): the country code given by user. It must be something similar to (BR, US, JP, FR)...
    
    Returns:
        bool: if it's empty, it returns True, else, returns False.
    """

    if city == "" or country_code == "":
        customized_message_box.custom_message_box("ERROR", "You must type a city and a country to continue!")
        return True
    return False
        

def handle_country_code_mistypes(country_code):
    """
    Verifies if the country code given is valid.
    
    Args:
        country_code (str): the country code given by user.
    
    Returns:
        bool: if it's not alphabetic and not exactly two numbers, it returns True, else, returns False.
    """
    
    # handles when user input is not an expected info for the API
    if not country_code.isalpha() or len(country_code) != 2:
        customized_message_box.custom_message_box("ERROR", "Country code must be exactly two alphabetic characters!")
        return True
    return False

def handle_no_data_found_error(forecast_result):
    """
        Verifies if the API's data returned successfully.
    
        Args:
            forecast_result: holds the API's request result, it can return None if the given input is invalid or return the data.
    
        Returns:
            bool: if it's None, it returns True, else, returns False.
    """
    
    if forecast_result is None:
        customized_message_box.custom_message_box("NOT FOUND", "The country or city typed cannot be found!")
        return True
    return False