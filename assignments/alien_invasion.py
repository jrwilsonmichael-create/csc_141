import sys 
import pygame
from settings import Settings
from ship import Ship
#from healthbar import HealthBar

class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((720,480))
        pygame.display.set_caption("Alien Infection")
        self.bg_color = (0, 35, 102)
        
        self.clock = pygame.time.Clock()
        self.clock.tick(60)
        self.ship = Ship(self)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:            
                if event.key == pygame.K_RIGHT:
                    # Move the ship to the right.               
                    self.ship.rect.x += 1

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.ship.blitme()
            #self.screen.fill(self.settings.bg_color)
            
                # Make the most recently drwn screen visible.
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()


