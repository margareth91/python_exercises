import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard


def run_game():
    # Inicjalizacja PyGame, ustawien i obiektu ekranu
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Inwazja obcych")

    # Utworzenie przycisku Gra
    play_button = Button(ai_settings, screen, "Start")

    # Utworzenie egzemplarzy przeznaczonych do przechowywania danych statystycznych gry
    stats = GameStats(ai_settings)
    sb = ScoreBoard(ai_settings, screen, stats)

    # Utworzenie statku kosmicznego, grupy pociskow oraz grupy obcych
    ship = Ship(ai_settings, screen)
    aliens = Group()
    bullets = Group()

    # Utworzenie floty obcych
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Rozpoczecie petli glownej gry
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
