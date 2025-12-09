# I will add city names function
def city_country(city, country):
    """Return a city and country formatted as 'City, Country'."""
    return f"{city.title()}, {country.title()}"
# Example usage
city = city_country('Tokyo', 'Japan')
print(city)