import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Testy dla progrmau 'name_function.py'"""

    def test_first_last_name(self):
        """Czy dane w postaci 'Kotek Miau' sa obslugiwane prawidlowo?"""
        formatted_name = get_formatted_name("kotek", "miau")
        self.assertEqual(formatted_name, "Kotek Miau")

    def test_first_middle_last_name(self):
        """Czy dane w postaci 'Kotek Miau Miau sa obslugiwane prawidlowo?"""
        formatted_name = get_formatted_name("kotek", "miau", "miau")
        self.assertEqual(formatted_name, "Kotek Miau Miau")


if __name__ == "__main__":
    unittest.main()
