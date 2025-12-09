# I will create my rocket class here
class Rocket:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 10 #speed of how fast the rocket moves
        self.rect = pygame.Rect(self.x, self.y, 10, 10)
        def update(self):
            """Move the rocket up the screen."""
            self.y -= self.speed
            self.rect.y = self.y
            def draw(self, screen):
                """Draw the rocket to the screen."""
                pygame.draw.rect(screen, (255, 0, 0), self.rect)  # Draw the rocket as a rectangle