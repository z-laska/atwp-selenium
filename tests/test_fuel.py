import unittest
from src.fuel_calculator import calculate_fuel


class TestLogin(unittest.TestCase):
    def test_mass_12(self):
        self.assertEqual(2, calculate_fuel(12))

    def test_mass_14(self):
        self.assertEqual(2, calculate_fuel(14))

    def test_mass_969(self):
        self.assertEqual(654, calculate_fuel(1969))

    def test_mass_100756(self):
        self.assertEqual(33583, calculate_fuel(100756))


if __name__ == '__main__':
    unittest.main()
