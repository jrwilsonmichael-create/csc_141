# I will create a health bar
import pygame
class HealthBar:
    """A class to manage the health bar."""
    def __init__(self, ai_game):
        """Initialize the health bar and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Set the dimensions and properties of the health bar.
        self.width, self.height = 200, 20
        self.health_color = (0, 255, 0)  # Green color for health
        self.border_color = (255, 255, 255)  # White border
        self.max_health = 100
        self.current_health = self.max_health

        # Create a rect for the health bar.
        self.rect = pygame.Rect(10, 10, self.width, self.height)

    def update_health(self, amount):
        """Update the current health by a specified amount."""
        self.current_health += amount
        if self.current_health < 0:
            self.current_health = 0
        elif self.current_health > self.max_health:
            self.current_health = self.max_health

    def draw(self):
        """Draw the health bar on the screen."""
        # Calculate the width of the health portion.
        health_width = (self.current_health / self.max_health) * self.width
        health_rect = pygame.Rect(self.rect.x, self.rect.y, health_width, self.height)

        # Draw the health portion.
        pygame.draw.rect(self.screen, self.health_color, health_rect)

        # Draw the border.
        pygame.draw.rect(self.screen, self.border_color, self.rect, 2)