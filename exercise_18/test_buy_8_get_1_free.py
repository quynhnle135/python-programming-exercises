from buy_8_get_1_free import get_cost_of_coffee
import unittest


class TestBuy8Get1Free(unittest.TestCase):
    def test_1(self):
        self.assertEqual(get_cost_of_coffee(7, 2.50), 17.50)

    def test_2(self):
        self.assertEqual(get_cost_of_coffee(8, 2.50), 20.0)

    def test_3(self):
        self.assertEqual(get_cost_of_coffee(9, 2.50), 20.0)

    def test_4(self):
        self.assertEqual(get_cost_of_coffee(10, 2.50), 22.50)

    def test_5(self):
        for i in range(1, 4):
            self.assertEqual(get_cost_of_coffee(0, i), 0)
            self.assertEqual(get_cost_of_coffee(8, i), 8 * i)
            self.assertEqual(get_cost_of_coffee(9, i), 8 * i)
            self.assertEqual(get_cost_of_coffee(18, i), 16 * i)
            self.assertEqual(get_cost_of_coffee(19, i), 17 * i)
            self.assertEqual(get_cost_of_coffee(30, i), 27 * i)


if __name__ == "__main__":
    unittest.main()