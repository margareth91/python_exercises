from random import choice


class RandomWalk:
    """Klasa przeznaczona do wygenerowania bladzenia losowego"""

    def __init__(self, num_points=5000):
        """Inicjalizacja atrybutow bladzenia"""
        self.num_points = num_points

        # Punkt poczatkowy ma wspolrzedne (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Wygenerowanie wszystkich punktow dla bladzenia losowego"""

        # Wykonywanie krokow az do chwili osiagniecia oczekiwanej liczby punktow
        while len(self.x_values) < self.num_points:
            # Ustalanie kierunku oraz odleglosci do pokonania w tym kierunku
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Odrzucenie ruchow prowadzacych donikad
            if x_step == 0 and y_step == 0:
                continue

            # Ustalenie nastepnych wartosci X i Y
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
