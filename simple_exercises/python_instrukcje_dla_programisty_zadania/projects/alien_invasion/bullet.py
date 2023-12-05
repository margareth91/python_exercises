import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Klasa przeznaczona do zarzadzania pociskami wystrzeliwanymi przez statek"""

    def __init__(self, ai_settings, screen, ship):
        """Utworzenie obiektu pocisku w aktualnym polozeniu statku"""
        super().__init__()
        self.screen = screen

        # Utworzenie prostokata pocisku w punkcie (0, 0), a nastepnie zdefiniowanie dla niego odpowiedniego polozenia
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Polozenie pocisku jest zdefiniowane za pomoca wartosci zmiennoprzecinkowej
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Poruszanie pociskiem po ekranie"""
        # Uaktualnienie polozenia pocisku
        self.y -= self.speed_factor

        # Uaktualnienie polozenia prostokata pocisku
        self.rect.y = self.y

    def draw_bullet(self):
        """Wyswietlenie pocisku na ekranie"""
        pygame.draw.rect(self.screen, self.color, self.rect)
