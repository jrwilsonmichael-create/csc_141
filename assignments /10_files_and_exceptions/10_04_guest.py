# I will add guest function
def make_guest(first_name, last_name, age=None, city=None):
    """Return a dictionary representing a guest."""
    guest_dict = {
        'first_name': first_name.title(),
        'last_name': last_name.title()
    }
    if age is not None:
        guest_dict['age'] = age
    if city is not None:
        guest_dict['city'] = city.title()
    return guest_dict
# Example usage:
print(make_guest("Aragnith", "Rusty", "immortal", "Finland"))