# I will test a restaurant function
def restaurant_name(name, cuisine_type):
    """Return a string describing the restaurant."""
    return f"{name.title()} serves wonderful {cuisine_type.title()}."
# Example usage:
print(restaurant_name("Millers", "Casual Dining restaurant chain"))
