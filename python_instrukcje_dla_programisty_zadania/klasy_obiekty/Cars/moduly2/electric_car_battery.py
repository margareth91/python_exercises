"""Zestaw klas przeznaczonych do zaprezentowania samochodu o napedzie elektrycznym"""

from car import Car


class Battery:
    """Prosta proba modelowania akumulatora samochodu elektrycznego"""

    def __init__(self, battery_size=60):
        """Inicjalizacja atrybutow akumulatora"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Wyswietlenie informacji o wielkosci akumulatora"""
        print(f"Ten samochod ma akumulator o pojemnosci {self.battery_size} kWh.")

    def get_range(self):
        """Wyswietla informacje o zasiegu samochodu na podstawie pojemnosci akumulatora"""
        if self.battery_size == 70:
            car_range = 240
            message = f"Zasieg tego samochodu po pelnym ladowaniu wynosi okolo {car_range} km."
            print(message)
        elif self.battery_size == 85:
            car_range = 270
            message = f"Zasieg tego samochodu po pelnym ladowaniu wynosi okolo {car_range} km."
            print(message)
        else:
            print(
                "Nie posiadamy informacji o zasiegu samochodu dla zadanej pojemnosci akumulatora."
            )

        # message = f"Zasieg tego samochodu po pelnym ladowaniu wynosi okolo {car_range} km."
        # print(message)


class ElectricCar(Car):
    """Przedstawia cechy charakterystyczne samochodu elektrycznego"""

    def __init__(self, make, model, year):
        """Inicjalizacja atrybutow klasy nadrzednej.
        Nastepnie inicjalizacja atrybutow charakterystycznych dla samochodu elektrycznego
        """
        super().__init__(make, model, year)
        self.battery = Battery()
