import unittest
from tempertature_conversion import convertToFahrenheit, convertToCelcius


class TestTemperatureConversion(unittest.TestCase):
    def test_convert_to_celsius_1(self):
        self.assertEqual(convertToCelcius(0), -17.77777777777778)

    def test_convert_to_celsius_2(self):
        self.assertEqual(convertToCelcius(180), 82.22222222222223)

    def test_convert_to_fahrenheit_1(self):
        self.assertEqual(convertToFahrenheit(0), 32.0)

    def test_convert_to_fahrenheit_2(self):
        self.assertEqual(convertToFahrenheit(100), 212.0)


if __name__ == "__main__":
    unittest.main()

