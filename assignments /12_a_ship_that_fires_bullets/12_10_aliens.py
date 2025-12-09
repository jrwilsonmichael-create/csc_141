# I will make aliens to the game
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
    new_alien = Aliens('green', 5)
    aliens.append(new_alien)
# Print the first 5 aliens
for alien in aliens[:5]:
    print(alien.describe_alien())
