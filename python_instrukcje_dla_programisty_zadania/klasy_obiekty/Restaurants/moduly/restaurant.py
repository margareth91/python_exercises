class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.cuisine_type = cuisine_type
        self.restaurant_name = restaurant_name
        self.number_served = 0

    def describe_restaurant(self):
        print(
            f"Restauracja o nazwie: {self.restaurant_name} | rodzaj kuchni: {self.cuisine_type}"
        )

    def open_restaurant(self):
        print(f"Restauracja otwarta w godzinach 12-22")

    def read_number_served(self):
        print(
            f"Liczba obsluzonych klientow w restauracji {self.restaurant_name}: {self.number_served} klientow."
        )

    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self, served):
        self.number_served += served
