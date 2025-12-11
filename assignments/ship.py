# I will make a ship
import pygame

class Ship: 
    """A class to manage the ship."""
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('C:/Users/Mikey/OneDrive/Desktop/csc_141/assignments/12_a_ship_that_fires_bullets/ship.bmp')
        self.image = pygame.transform.scale(self.image, (40,60))  # width, height in pixels
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        
        # Movement flags; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)



 
    def update(self):

        """Update the ship's position based on movement flags."""
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # Update rect object from self.x.
        self.rect.x = self.x