def describe_city(city, country='Polska'):
    print(f"{city.title()} jest miastem lezacym na terenie kraju: {country.title()}")


describe_city('gdansk')
describe_city('warszawa')
describe_city('wieden', 'austria')


def city_country(city, country):
    print(f"{city.title()}, {country.title()}")


city_country('gdansk', 'polska')
city_country('warszawa', 'polska')
city_country('salzburg', 'austria')
city_country('bibione', 'wlochy')
