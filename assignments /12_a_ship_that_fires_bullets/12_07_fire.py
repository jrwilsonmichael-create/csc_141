# I will be making the ship fire bullets
import pygame
class Fire:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 15
        self.rect = pygame.Rect(self.x, self.y, 5, 15)
        def move(self):
            self.y -= self.speed
            self.rect.y = self.y
            def draw(self, screen):
                pygame.draw.rect(screen, (255, 0, 0), self.rect)  # Draw the fire as a rectangle