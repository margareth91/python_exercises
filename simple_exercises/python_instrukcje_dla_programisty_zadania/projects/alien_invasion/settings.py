class Settings:
    """Klasa przeznaczona do przechowywania wszystkich ustawien gry"""

    def __init__(self):
        """Inicjalizacja danych statystycznych gry"""
        # ustawienia ekranu
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (230, 230, 230)

        # Ustawienia dotyczace statku
        self.ship_limit = 3

        # Ustawienia dotyczace pocisku
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (128, 0, 0)
        self.bullets_allowed = 5
        # self.number_of_bullets = 3

        # Ustawienia dotyczace obcego
        self.fleet_drop_speed = 1

        # Latwa zmiana szybkosci gry
        self.speedup_scale = 1.1

        # Latwa zmiana przyznawanych punktow
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Inicjalizacja ustawien, ktore ulegaja zmianie w trakcie gry"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # Wartosc fleet_direction wynoszaca 1 oznacza prawo, a -1 oznacza lewo
        self.fleet_direction = 1

        # Punktacja
        self.alien_points = 50

    def new_level_settings(self):
        """Zmiana ustawien dotyczacych szybkosci i przyznawanych punktow"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        self.bullets_allowed += 1

    # def super_level_settings(self):
    #     self.number_of_bullets += 1
