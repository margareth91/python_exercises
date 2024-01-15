"""9.10. Zaimportowana klasa Restaurant. Przenieś do modułu ostatnią wersję klasy Restaurant i utwórz oddzielny plik
importujący tę klasę. Utwórz egzemplarz klasy Restaurant, a następnie wywołaj metodę tej klasy, aby sprawdzić,
czy polecenie import działa prawidłowo."""

from restaurant import Restaurant

restaurant1 = Restaurant("Kotki Psotki", "kocia kawiarnia")
restaurant1.describe_restaurant()
