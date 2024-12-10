# converts the kelvin degrees obtained to celsius
def kelvin_to_celsius(temperature):
    """
    Converts the Kelvin degrees obtained from the API to Celsius.
    
    Args:
        temperature (float): the value obtained from the API's data.
    
    Returns:
        float: the result converted into Celsius.
    """
    
    return temperature - 273.15
