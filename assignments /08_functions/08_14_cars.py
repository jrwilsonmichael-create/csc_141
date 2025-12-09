# I will be making a function that stores information about a car inn a dictonary
def car_info(manufacturer, model, **car_info):
    """Store information about a car in a dictionary.

    Args:
        manufacturer (str): The manufacturer of the car.
        model (str): The model of the car.
        **car_info: Additional keyword arguments representing other car details.

    Returns:
        dict: A dictionary containing the car's information.
    """
    car_dict = {
        'manufacturer': manufacturer,
        'model': model
    }
    for key, value in car_info.items():
        car_dict[key] = value
    return car_dict
# Example usage:
car = car_info('Toyota', 'AE86', color='white', year=1986, mileage=15000)
print(car)
# Output: {'manufacturer': 'Toyota', 'model': 'AE86', 'color': 'white', 'year': 1986, 'mileage': 15000}