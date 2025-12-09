# I will test cities function
def city_country(city, country):
    """Return a string formatted as 'City, Country'."""
    return f"{city.title()}, {country.title()}"
# Example usage:
print(city_country("philadelphia", "usa"))