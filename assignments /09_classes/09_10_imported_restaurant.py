# I will import the Restaurant class from another module
from classes._09_01_restaurant import Restaurant
# Create an instance of the Restaurant class
my_restaurant = Restaurant("Millers", "Casual Dining restaurant chain")
# Display the restaurant's details
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
print(f"Cuisine Type: {my_restaurant.cuisine_type}")