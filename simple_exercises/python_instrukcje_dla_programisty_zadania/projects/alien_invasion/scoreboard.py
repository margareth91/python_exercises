import pygame.font
from pygame.sprite import Group
from ship import Ship


class ScoreBoard:
    """Klasa przeznaczona do przedstawiania informacji o punktacji"""

    def __init__(self, ai_settings, screen, stats):
        """Inicjalizacja atrybutow dotyczacych punktacji"""
        self.stats = stats
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        # Ustawienia czcionki dla informacji dotyczacych punktacji
        self.text_color = (128, 0, 0)
        self.font = pygame.font.SysFont(None, 48)

        # Przygotowanie poczatkowych obrazow z punktacja
        self.prep_images()

    def prep_score(self):
        """Przeksztalcenie puktacji na wygenerowany obraz"""
        rounded_score = round(int(self.stats.score), -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render("Score: " + score_str, True, self.text_color, self.ai_settings.bg_color)

        # Wyswietlenie punktacji w prawym gornym rogu ekranu
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Wyswietlenie na ekranie punktacji oraz statkow"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

        # Wyswietlenie statkow
        self.ships.draw(self.screen)

    def prep_high_score(self):
        """Konwersja najlepszego wyniku w grze na wygenerowany obraz"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render("Best Score: " + high_score_str, True, self.text_color,
                                                 self.ai_settings.bg_color)

        # Wyswietlenie najlepszego wyniku w grze na srodku ekranu, przy gornej krawedzi
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Konwersja numeru poziomu na wygenerowany obraz"""
        self.level_image = self.font.render("Level: " + str(self.stats.level), True, self.text_color,
                                            self.ai_settings.bg_color)

        # Numer poziomu wyswietlany pod aktualna punktacja
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Wyswietla liczbe statkow, jakie pozostaly graczowi"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def save_hs_to_file(self, high_score):
        # Zapisanie najlepszego wyniku do pliku w celu przechowania po zamknieciu okna gry
        filename = 'high_score.txt'

        with open(filename, 'w') as file_object:
            file_object.write(str(high_score))

    def prep_images(self):
        # Przygotowanie poczatkowych obrazow
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
