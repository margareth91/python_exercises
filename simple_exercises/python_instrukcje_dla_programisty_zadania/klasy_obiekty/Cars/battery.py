class Car:

    def __init__(self, make, model, year):
        self.year = year
        self.model = model
        self.make = make
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print(f"Ten samochod ma przejechane {self.odometer_reading} km.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Nie mozna cofnac licznika przebiegu samochodu!")

    def increment_odometer(self, kilometers):
        self.odometer_reading += kilometers


class Battery:

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"Ten samochod ma akumulator o pojemnosci {self.battery_size} kWh.")

    def get_range(self):
        if self.battery_size == 70:
            car_range = 240
        elif self.battery_size == 85:
            car_range = 270

        message = f"Zasieg tego samochodu wynosi okolo {car_range} km po pelnym naladowaniu akumulatora."
        print(message)

    def upgrade_battery(self):
        if self.battery_size == 70:
            self.battery_size = 85


class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_new_car = ElectricCar('bmw', 'seria x7', 2023)
print(my_new_car.get_descriptive_name())
my_new_car.battery.get_range()
my_new_car.battery.upgrade_battery()
my_new_car.battery.get_range()
