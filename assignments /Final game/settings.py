# I will add settings for my game here.


class Settings:
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 720
        self.screen_height = 480
        self.bg_color = (0, 35, 102)

        # Ship settings
        # Increase speed slightly for more responsive movement
        self.ship_speed = 2.5

        # Bullet settings
        self.bullet_speed = 4.0
        self.bullet_width = 3
        self.bullet_height = 15
        # Make bullets bright white and a bit faster
        self.bullet_color = (255, 255, 255)
      # Bullet settings
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 3


        # Alien settings
        self.alien_speed = 1.0

        # Alien settings
        self.alien_speed = 1.0
        # How many pixels the fleet drops when reaching an edge
        self.fleet_drop_speed = 1
    # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1