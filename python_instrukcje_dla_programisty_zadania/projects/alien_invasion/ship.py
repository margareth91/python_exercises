import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """Inicjalizacja statku kosmicznego i jego polozenie poczatkowe"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Wczytanie obrazu statku kosmicznego i pobranie jego prostokata
        self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.smoothscale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Kazdy nowy statek kosmiczny pojawia sie na dole ekranu
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Punkt srodkowy statku jest przechowywany w postaci liczby zmiennoprzecinkowej
        self.center = float(self.rect.centerx)

        # Opcje wskazujace na poruszanie sie statku
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Uaktualnienie polozenia statku na podstawie opcji wskazujacej jego ruch"""
        # Uaktualnienie wartosci punktu srodkowego statku, a nie jego prostokata
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Uaktualnienie obiektu rect na podstawie wartosci self.center
        self.rect.centerx = self.center

    def blitme(self):
        # Wyswietlenie statku kosmicznego w jego aktualnym polozeniu
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Umieszczenie statku na srodku przy dolnej krawedzi ekranu"""
        self.center = self.screen_rect.centerx
