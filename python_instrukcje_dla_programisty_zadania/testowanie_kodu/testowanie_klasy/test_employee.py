import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("Jan", "Kowalski", 100000)
        self.custom_raise = 10000

    def test_give_default_raise(self):
        raised_annual_compensation = self.employee.give_raise()
        self.assertEqual(raised_annual_compensation, self.employee.give_raise())

    def test_give_custom_raise(self):
        raised_annual_compensation = self.employee.give_raise(self.custom_raise)
        self.assertEqual(
            raised_annual_compensation, self.employee.give_raise(self.custom_raise)
        )


if __name__ == "__main__":
    unittest.main()
