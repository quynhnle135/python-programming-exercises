import unittest
from hours_minutes_seconds import get_hours_minutes_seconds


class TestHoursMinutesSeconds(unittest.TestCase):
    def test_1(self):
        self.assertEqual(get_hours_minutes_seconds(30), '30s')

    def test_2(self):
        self.assertEqual(get_hours_minutes_seconds(60), '1m')

    def test_3(self):
        self.assertEqual(get_hours_minutes_seconds(90), '1m 30s')

    def test_4(self):
        self.assertEqual(get_hours_minutes_seconds(3600), '1h')

    def test_5(self):
        self.assertEqual(get_hours_minutes_seconds(3601), '1h 1s')

    def test_6(self):
        self.assertEqual(get_hours_minutes_seconds(3661), '1h 1m 1s')

    def test_7(self):
        self.assertEqual(get_hours_minutes_seconds(90042), '25h 42s')

    def test_8(self):
        self.assertEqual(get_hours_minutes_seconds(0), '0s')
