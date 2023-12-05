class GameStats:
    """Monitorowanie danych statystycznych dla gry"""

    def __init__(self, ai_settings):
        """Inicjalizacja danych statystycznych"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Uruchomienie gry w stanie nieaktywnym
        self.game_active = False
        self.high_score = self.read_hs_from_file()

    def reset_stats(self):
        """Inicjalizacja danych statystycznych, ktore moga zmieniac sie w trakcie gry"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def read_hs_from_file(self):
        # Wczytanie najlepszego wyniku z pliku
        filename = 'high_score.txt'

        with open(filename) as file_object:
            high_score = file_object.read()
        return int(high_score)
