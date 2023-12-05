class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.cuisine_type = cuisine_type
        self.restaurant_name = restaurant_name
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restauracja o nazwie: {self.restaurant_name} | rodzaj kuchni: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Restauracja otwarta w godzinach 12-22")

    def read_number_served(self):
        print(f"Liczba obsluzonych klientow w restauracji {self.restaurant_name}: {self.number_served} klientow.")

    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self, served):
        self.number_served += served


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['cytrynowy', 'czekoladowy', 'waniliowy', 'malinowy', 'jogurtowo-porzeczkowy', 'mascarpone']

    def read_flavors(self):
        print(f"Smaki lodow dostepne w lodziarni: {self.flavors}")


ice_cream_stand1 = IceCreamStand('Lodusiowo', 'lodziarnia')
ice_cream_stand1.describe_restaurant()
ice_cream_stand1.read_flavors()
