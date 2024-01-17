import unittest
from city_functions import get_city_country


class TestCityCountry(unittest.TestCase):
    def test_city_country(self):
        city_country = get_city_country("warszawa", "polska")
        self.assertEqual(city_country, "Warszawa, Polska")

    def test_city_country_population(self):
        city_country = get_city_country("santiago", "chile", "5000000")
        self.assertEqual(city_country, "Santiago, Chile, population - 5000000")


if __name__ == "__main__":
    unittest.main()
