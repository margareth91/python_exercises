"""Klasa, ktora bedzie wykorzystywana do zaprezentowania samochodu"""


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
