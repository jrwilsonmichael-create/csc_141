# I will add a population
def city_country(city, country, population=None):
    """Return a string formatted as 'City, Country - population xxx' if population is provided."""
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city.title()}, {country.title()}"
# Example usage:
print(city_country("Philadelphia", "USA", 1584200))
print(city_country("Tokyo", "Japan"))