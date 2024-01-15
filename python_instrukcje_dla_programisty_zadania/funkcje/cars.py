"""8.14. Samochody. Utwórz funkcję przechowującą w słowniku informacje o samochodzie. Ta funkcja zawsze powinna
otrzymywać nazwy marki i modelu pojazdu, po którym można podać dowolną liczbę argumentów w postaci słów kluczowych.
Wywołaj funkcję zawierającą wymagane informacje oraz dwie dodatkowe pary nazwa-wartość, na przykład opisujące kolor
i wyposażenie dodatkowe. Przygotowana funkcja powinna być wywoływana w sposób podobny do przedstawionego poniżej:
car = make_car('subaru', 'outback', color='blue', tow_package=True)
Wyświetl zawartość słownika zwróconego przez tę funkcję i upewnij się, że wszystkie podane informacje zostały w nim
prawidłowo zapisane."""


def make_cars_list(make, model, **car_info):
    car_profile = {}
    car_profile["make"] = make
    car_profile["model"] = model
    for key, value in car_info.items():
        car_profile[key] = value
    return car_profile


car1 = make_cars_list("bmw", "x1", color="red", car_mileage="200000 km")
print(car1)
