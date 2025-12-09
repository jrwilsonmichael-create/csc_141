# I will be shooting aliens
import random
class Alien:
    def __init__(self, color, points):
        self.color = color
        self.points = points

    def describe_alien(self):
        description = f"Alien Color: {self.color}, Points: {self.points}"
        return description
class Bullet:
    def __init__(self, speed):
        self.speed = speed

    def describe_bullet(self):
        return f"Bullet Speed: {self.speed}"
def shoot_alien(alien, bullet):
    hit_chance = random.random()
    if hit_chance < 0.7:  # 70% chance to hit
        return True
    else:
        return False