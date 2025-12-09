# I will be printing models of cars using a function
def print_car_models(manufacturer, *models):
    """Prints the car models for a given manufacturer.

    Args:
        manufacturer (str): The manufacturer of the cars.
        *models: Variable length argument list of car models.
    """
    print(f"Car models from {manufacturer.title()}:")
    for model in models:
        print(f"- {model.title()}")
# Example usage:
print_car_models('ford', 'mustang', 'f-150', 'explorer')