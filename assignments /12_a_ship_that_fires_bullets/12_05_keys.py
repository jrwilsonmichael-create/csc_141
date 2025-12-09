# I will be adding keys 
import pygame
class ship:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.speed = 5
		self.rect = pygame.Rect(self.x, self.y, 50, 50)
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
	def update(self):
		"""Update the ship's position based on movement flags."""
		if self.moving_right:
			self.x += self.speed
		if self.moving_left:
			self.x -= self.speed
		if self.moving_up:
			self.y -= self.speed
		if self.moving_down:
			self.y += self.speed
			self.rect.x = self.x
			self.rect.y = self.y
		def draw(self, screen):
			"""Draw the ship to the screen."""
			pygame.draw.rect(screen, (0, 0, 255))
			(self.rect) # Draw the ship as a rectangle