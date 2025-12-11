import pygame


class HealthBar:
    """A simple health bar drawn on the screen.

    Usage: create with `HealthBar(ai_game, max_health=100)` and call
    `healthbar.blitme()` each frame. Use `healthbar.update(value)` to
    change current health.
    """

    def __init__(self, ai_game, max_health=100):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = getattr(ai_game, 'settings', None)

        self.max_health = max_health
        self.current = max_health

        # Visual settings
        self.width = 200
        self.height = 18
        self.padding = 6
        self.border_color = (255, 255, 255)
        self.fill_color = (0, 200, 0)
        self.bg_color = (40, 40, 40)

        # Position at top-right with a margin
        margin = 12
        self.x = self.screen_rect.right - self.width - margin
        self.y = margin
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self, value):
        """Set current health (clamped between 0 and max_health)."""
        self.current = max(0, min(self.max_health, value))

    def blitme(self):
        """Draw the healthbar on the screen."""
        # Background
        bg_rect = pygame.Rect(self.rect.x - 1, self.rect.y - 1, self.rect.width + 2, self.rect.height + 2)
        pygame.draw.rect(self.screen, self.bg_color, bg_rect)

        # Filled portion
        pct = self.current / self.max_health if self.max_health else 0
        fill_width = int(self.rect.width * pct)
        fill_rect = pygame.Rect(self.rect.x, self.rect.y, fill_width, self.rect.height)
        pygame.draw.rect(self.screen, self.fill_color, fill_rect)

        # Border
        pygame.draw.rect(self.screen, self.border_color, self.rect, 2)

        # Optional: draw numeric text (requires pygame.font)
        try:
            font = pygame.font.SysFont(None, 16)
            text = f"{int(self.current)}/{int(self.max_health)}"
            text_surf = font.render(text, True, self.border_color)
            text_rect = text_surf.get_rect(center=self.rect.center)
            self.screen.blit(text_surf, text_rect)
        except Exception:
            pass