import pygame, sys

# I will create my game character class here.
class GameCharacter:
    def __init__(self, name, health, position):
        self.name = name
        self.health = health
        self.position = position 
        self.bullets = []
        self.is_alive = True
        self.score = 0
        self.level = 1
        self.speed = 5
        self.direction = (0, 1)
        self.invetory = []
        self.abilities = []
        self.experience = 0
        self.mana = 100
        self.stamina = 100
        self.armor = 0
        self.weapon = None
        self.is_jumping = False
        self.is_running = False
        self.is_shooting = False
        self.is_crouching = False
        self.is_reloading = False
        self.is_interacting = False
        self.is_aiming = False

    
    pygame.init()

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game assets and behavior."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (0, 35, 102)  # Royal blue color for the sky

    def run_game(self):
        """start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.screen.fill(self.bg_color)  # Fill the screen with the sky color

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()