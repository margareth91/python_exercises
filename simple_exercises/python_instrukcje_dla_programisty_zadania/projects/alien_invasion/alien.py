import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Klasa przedstawiajaca pojedynczego obcego we flocie"""

    def __init__(self, ai_settings, screen):
        """Inicjalizacja obcego i zdefiniowanie jego polozenia poczatkowego"""
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        # Wczytanie obrazu obcego i zdefiniowanie jego atrybutu rect
        self.image = pygame.image.load('images/alien.bmp')
        self.image = pygame.transform.smoothscale(self.image, (50, 50))
        self.rect = self.image.get_rect()

        # Umieszczenie nowego obcego w poblizu lewego gornego rogu ekranu
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Przechowywanie dokladnego polozenia obcego
        self.x = float(self.rect.x)

    def blitme(self):
        """Wyswietlenie obcego w jego aktualnym polozeniu"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Przesuniecie obcego w prawo lub w lewo"""
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """Zwraca True, jesli obcy znajduje sie przy krawedzi ekranu"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
