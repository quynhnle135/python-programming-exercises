import unittest
from change_maker import make_change


class TestChangeMaker(unittest.TestCase):
    def test_1(self):
        self.assertEqual(make_change(30), {'quarters': 1, 'nickles': 1})

    def test_2(self):
        self.assertEqual(make_change(10), {'dimes': 1})

    def test_3(self):
        self.assertEqual(make_change(57), {'quarters': 2, 'nickles': 1, 'pennies': 2})

    def test_4(self):
        self.assertEqual(make_change(100), {'quarters': 4})

    def test_5(self):
        self.assertEqual(make_change(125), {'quarters': 5})


if __name__ == "__main__":
    unittest.main()