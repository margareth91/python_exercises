"""11.1. Miasto, państwo. Przygotuj funkcję akceptującą dwa parametry: nazwy miasta i państwa. Wartością zwrotną tej
funkcji powinien być pojedynczy ciąg tekstowy w postaci Miasto, Państwo, na przykład Santiago, Chile. Gotową
funkcję umieść w module o nazwie city_functions.py.

Utwórz plik o nazwie test_cities.py przeznaczony do przetestowania przygotowanej wcześniej funkcji (pamiętaj
o konieczności zaimportowania modułu unittest oraz funkcji, która ma zostać sprawdzona). Następnie w pliku
test_cities.py zdefiniuj funkcję o nazwie test_city_country() odpowiedzialną za sprawdzenie, czy wywołanie
utworzonej w poprzednim ćwiczeniu funkcji, na przykład z wartościami 'santiago' i 'chile', spowoduje wygenerowanie
oczekiwanego ciągu tekstowego. Uruchom plik test_cities.py i upewnij się, że test test_city_country() zostaje zaliczony.

11.2. Populacja. Zmodyfikuj przygotowaną wcześniej funkcję, aby wymagała podania trzeciego argumentu — populacji
(population). Teraz wartością zwrotną funkcji powinien być ciąg tekstowy w postaci Miasto, Państwo - populacja xxx,
na przykład Santiago, Chile - populacja 5000000. Ponownie uruchom test_cities.py. Upewnij się, że tym razem test
zdefiniowany w metodzie test_city_country() będzie niezaliczony.

Zmodyfikuj funkcję, aby parametr population był opcjonalny. Ponownie uruchom test_cities.py i upewnij się,
że również teraz test zdefiniowany w metodzie test_city_country() zostanie zaliczony.

Utwórz drugi test o nazwie test_city_country_population(), sprawdzający, czy można wywołać funkcję z wartościami
'santiago', 'chile' i 'population=5000000'. Raz jeszcze uruchom test_cities.py i upewnij się, że nowy test został
zaliczony."""


def get_city_country(city, country, population=""):
    if population:
        city_country = f"{city.title()}, {country.title()}, population - {population}"
    else:
        city_country = f"{city.title()}, {country.title()}"
    return city_country
