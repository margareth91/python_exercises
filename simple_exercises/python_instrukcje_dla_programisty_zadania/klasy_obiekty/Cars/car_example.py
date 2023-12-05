"""Klasa, ktora bedzie uzywana do zaprezentowania samochodu"""


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
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Wyswietla informacje o przebiegu samochodu"""
        print(f"Ten samochod ma przejechane {self.odometer_reading} km.")

    def update_odometer(self, mileage):
        """Przypisanie podanej wartosci licznikowi przebiegu samochodu.
        Zmiana zostanie odrzucona w przypadku proby cofniecia licznika"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Nie mozna cofnac licznika przebiegu samochodu!")

    def increment_odometer(self, kilometers):
        """Inkrementacja wartosci licznika przebiegu samochodu o podana wartosc"""
        self.odometer_reading += kilometers


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_new_car.update_odometer(50)
my_new_car.read_odometer()
my_new_car.update_odometer(100)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()