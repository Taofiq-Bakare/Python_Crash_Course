

def city_name(city, country, population=''):
    """
    A simple function to format city names
    """
    if population:
        location = f"{city}, {country} - population {population}"
    else:
        location = f"{city}, {country}"
    return location.title()
