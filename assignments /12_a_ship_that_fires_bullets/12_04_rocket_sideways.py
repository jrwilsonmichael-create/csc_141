# I will create a rocket that moves sideways.
class SidewaysRocket:
    def __init__(self, position, speed=10, damage=50):
        self.position = position
        self.speed = speed
        self.damage = damage
        self.is_active = True
        self.explosion_radius = 5
        self.fuel = 100
        self.is_homing = False
        self.target = None
        self.is_exploding = False
        self.explosion_damage = 100
        self.explosion_effect = None

    def move(self):
        if self.is_active and self.fuel > 0:
            # Move the rocket sideways (to the right)
            self.position = (self.position[0] + self.speed, self.position[1])
            self.fuel -= 1
        else:
            self.is_active = False