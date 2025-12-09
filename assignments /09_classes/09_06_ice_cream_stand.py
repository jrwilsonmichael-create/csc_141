# Ice Cream Stand
class IceCreamStand:
    def __init__(self, name, cuisine_type, flavors):
        self.name = name
        self.cuisine_type = cuisine_type
        self.flavors = flavors

    def display_flavors(self):
        print(f"Available flavors at {self.name}:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")
# Example usage:
ice_cream_stand = IceCreamStand("Sweet Treats", "Ice Cream", ["vanilla", "cookies and cream", "strawberry"])
ice_cream_stand.display_flavors()