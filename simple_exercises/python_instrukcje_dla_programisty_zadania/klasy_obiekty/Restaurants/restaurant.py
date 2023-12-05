
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


new_restaurant1 = Restaurant("Sushi Love", "azjatycka")
new_restaurant1.describe_restaurant()
new_restaurant1.open_restaurant()

new_restaurant2 = Restaurant("Rodzinna", "tradycyjna")
new_restaurant3 = Restaurant("EmSiKurczak", "fast food")
new_restaurant4 = Restaurant("AsiaFusion", "azjatycka")

new_restaurant2.describe_restaurant()
new_restaurant3.describe_restaurant()
new_restaurant4.describe_restaurant()

new_restaurant1.read_number_served()
new_restaurant2.read_number_served()
new_restaurant3.read_number_served()
new_restaurant4.read_number_served()

new_restaurant1.set_number_served(5)
new_restaurant1.read_number_served()
new_restaurant1.set_number_served(5)
new_restaurant1.read_number_served()
new_restaurant1.increment_number_served(15)
new_restaurant1.read_number_served()
new_restaurant1.increment_number_served(50)
new_restaurant1.read_number_served()
new_restaurant1.increment_number_served(100)
new_restaurant1.read_number_served()
