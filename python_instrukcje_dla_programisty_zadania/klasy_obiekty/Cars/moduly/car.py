# """Klasa, ktora bedzie wykorzystywana do zaprezentowania samochodu"""
"""Zestaw klas przeznaczonych do zaprezentowania samochodu, zarowno o napedzie tradycyjnym, jak i elektrycznym"""


class Car:
    """Prosta proba zaprezentowania samochodu"""

    def __init__(self, make, model, year):
        """Inicjalizacja atrybutow opisujacych samochod"""
        self.year = year
        self.model = model
        self.make = make
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Zwrot elegancko sformatowanego opisu samochodu"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Wyswietla informacje o przebiegu samochodu"""
        print(f"Ten samochod ma przejechane {self.odometer_reading} km.")

    def update_odometer(self, mileage):
        """Przypisanie podanej wartosci licznikowi przebiegu samochodu.
        Zmiana zostanie odrzucona w przypadku proby cofniecia licznika."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Nie mozna cofnac licznika przebiegu samochodu!")

    def increment_odometer(self, kilometers):
        """Inkrementacja wartosci licznika przebiegu samochodu o podana wartosc"""
        self.odometer_reading += kilometers


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
