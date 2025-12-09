# I will be makking bullets for my ship
import pygame
class bullets:
    def __init__(self, screen):
        self.screen = screen
        self.bullets = []

    def update(self):
        for bullet in self.bullets:
            bullet.update()
    def draw(self):
        for bullet in self.bullets:
            bullet.draw(self.screen)
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Bullets Example")
    bullets_group = bullets(screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        bullets_group.update()
        screen.fill((0, 0, 0))
        bullets_group.draw()
        pygame.display.flip()
        pygame.quit()
    
    if __name__ == "__main__":
        main()