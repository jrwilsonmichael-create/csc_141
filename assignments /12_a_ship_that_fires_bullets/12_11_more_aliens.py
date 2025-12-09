# I will add more aliens to the game with different colors and points
class Aliens:
    def __init__(self, color, points):
        self.color = color
        self.points = points

    def describe_alien(self):
        description = f"Alien Color: {self.color}, Points: {self.points}"
        return description
# Create a list of aliens
aliens = []
for alien_number in range(30):
    if alien_number < 10:
        new_alien = Aliens('green', 5)
    elif alien_number < 20:
        new_alien = Aliens('yellow', 10)
    else:
        new_alien = Aliens('red', 15)
    aliens.append(new_alien)
# Print the first 5 aliens
for alien in aliens[:5]:
    print(alien.describe_alien())