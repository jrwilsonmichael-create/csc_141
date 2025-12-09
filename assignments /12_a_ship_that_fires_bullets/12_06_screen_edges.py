# I will make the screen edges wrap around for the ship
import pygame 
from pygame.locals import *
from ship import Ship
from bullet import Bullet
from settings import Settings
from game import Game
from screen_edges import ScreenEdges
def main():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height)
    )
    pygame.display.set_caption("A Ship That Fires Bullets with Screen Edges")
    ship = Ship(screen, settings)
    bullets = pygame.sprite.Group()
    screen_edges = ScreenEdges(screen, settings)
    game = Game(screen, settings, ship, bullets, screen_edges)
    game.run_game()