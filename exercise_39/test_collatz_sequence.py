import unittest
from collatz_sequence import generate_collatz_sequence


class TestCollatzSequence(unittest.TestCase):
    def test_1(self):
        self.assertEqual(generate_collatz_sequence(0), [])

    def test_2(self):
        self.assertEqual(generate_collatz_sequence(10), [10, 5, 16, 8, 4, 2, 1])

    def test_3(self):
        self.assertEqual(generate_collatz_sequence(12), [12, 6, 3, 10, 5, 16, 8, 4, 2, 1])


if __name__ == "__main__":
    unittest.main()