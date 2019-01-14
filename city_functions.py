"""
A simple class that stores a city and country in a formatted string.

Author: Oscar Lopez
Date: Jan 13, 2019
"""

def set_location(city_name,country_name,state=''):
    if state:
        location = city_name.title() + ", " + state.title() + ", " + country_name.title()
    else:
        location = city_name.title() + ", " + country_name.title()
    return location
