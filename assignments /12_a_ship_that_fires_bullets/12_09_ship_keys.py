# I will add ship keys to move the ship
import pygame
class ShipKeys:
    def __init__(self, ship):
        self.ship = ship
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.ship.rect.right < self.ship.screen.get_rect().right:
            self.ship.rect.x += self.ship.settings.ship_speed
        if self.moving_left and self.ship.rect.left > 0:
            self.ship.rect.x -= self.ship.settings.ship_speed