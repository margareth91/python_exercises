"""8.5. Miasta. Utwórz funkcję o nazwie describe_city(), akceptującą nazwę miasta i kraju. Ta funkcja powinna wyświetlać
proste zdanie, takie jak „Warszawa leży w Polsce”. Parametrowi przechowującemu nazwę państwa przypisz wartość domyślną.
Przygotowaną funkcję wywołaj dla trzech różnych miast, z których przynajmniej jedno nie powinno być położone w domyślnie
zdefiniowanym kraju.

8.6. Nazwy miast. Utwórz funkcję o nazwie city_country() pobierającą nazwę miasta i kraju, w którym ono leży. Wartością
zwrotną funkcji powinien być ciąg tekstowy sformatowany w poniższy sposób:
Santiago, Chile
Przygotowaną funkcję wywołaj z przynajmniej trzema parami miasto-państwo i wyświetl wygenerowaną przez nie wartość."""


def describe_city(city, country="Polska"):
    print(f"{city.title()} jest miastem lezacym na terenie kraju: {country.title()}")


describe_city("gdansk")
describe_city("warszawa")
describe_city("wieden", "austria")


def city_country(city, country):
    print(f"{city.title()}, {country.title()}")


city_country("torun", "polska")
city_country("warszawa", "polska")
city_country("salzburg", "austria")
city_country("wenecja", "wlochy")
