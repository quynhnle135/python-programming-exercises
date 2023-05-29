import unittest
from area_and_volume import area, perimeter, surface_area, volume


class TestAreaAndVolume(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(10, 10), 100)
        self.assertEqual(area(0, 9999), 0)
        self.assertEqual(area(5, 8), 40)

    def test_perimeter(self):
        self.assertEqual(perimeter(10, 10), 40)
        self.assertEqual(perimeter(0, 9999), 19998)
        self.assertEqual(perimeter(5, 8), 26)

    def test_volume(self):
        self.assertEqual(volume(10, 10, 10), 1000)
        self.assertEqual(volume(9999, 0, 9999), 0)
        self.assertEqual(volume(5, 8, 10), 400)

    def test_surface_area(self):
        self.assertEqual(surface_area(10, 10, 10), 600)
        self.assertEqual(surface_area(9999, 0, 9999), 199960002)
        self.assertEqual(surface_area(5, 8, 10), 340)


if __name__ == "__main__":
    unittest.main()

