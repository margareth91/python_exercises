"""9.1. Restauracja. Przygotuj klasę o nazwie Restaurant. Metoda __init__() w klasie Restaurant powinna przechowywać
dwa atrybuty: restaurant_name i cuisine_type. Utwórz metodę o nazwie describe_restaurant() wyświetlającą te dwa
fragmenty informacji oraz metodę o nazwie open_restaurant() wyświetlającą informacje o godzinach pracy restauracji.
Na podstawie przygotowanej klasy utwórz egzemplarz restaurant. Wyświetl oddzielnie oba atrybuty, a następnie wywołaj
obie metody.

9.2. Trzy restauracje. Pracę rozpocznij od klasy opracowanej w ćwiczeniu 9.1. Utwórz trzy różne egzemplarze
na podstawie tej klasy, a następnie wywołaj metodę describe_restaurant() dla każdego egzemplarza.

9.4. Liczba obsłużonych. Pracę rozpocznij od programu utworzonego w ćwiczeniu 9.1. Dodaj atrybut o nazwie
number_served o wartości domyślnej 0. Następnie na podstawie klasy utwórz egzemplarz o nazwie restaurant. Wyświetl
liczbę klientów obsłużonych przez restaurację, zmień tę wartość i później wyświetl nową.

Dodaj metodę o nazwie
set_number_served(), pozwalającą na zdefiniowanie liczby obsłużonych klientów. Wywołaj tę metodę wraz z różnymi wartościami
i je wyświetl.

Dodaj metodę o nazwie increment_number_served(), pozwalającą na inkrementację wartości wskazującej na liczbę
obsłużonych klientów. Wywołaj tę metodę dowolną ilość razy, symulując w ten sposób liczbę klientów obsłużonych
na przykład w ciągu dnia roboczego."""


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
