import unittest
from sum_and_product import calculate_product, calculate_sum


class TestSumAndProduct(unittest.TestCase):
    def test_sum_1(self):
        self.assertEqual(calculate_sum([1, 2, 3, 4, 5]), 15)

    def test_sum_2(self):
        self.assertEqual(calculate_sum([2, 4, 6, 8, 10]), 30)

    def test_sum_3(self):
        self.assertEqual(calculate_sum([1, 1, 1, 1, 1]), 5)

    def test_product_1(self):
        self.assertEqual(calculate_product([1, 1, 1, 1, 1]), 1)

    def test_product_2(self):
        self.assertEqual(calculate_product([1, 2, 3, 4, 5]), 120)

    def test_product_3(self):
        self.assertEqual(calculate_product([2, 4, 6, 8, 10]), 3840)


if __name__ == "__main__":
    unittest.main()