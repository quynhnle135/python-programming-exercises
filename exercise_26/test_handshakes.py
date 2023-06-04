import unittest
from handshakes import count_handshakes


class TestHandShakes(unittest.TestCase):
    def test_1(self):
        self.assertEqual(count_handshakes(['Alice', 'Bob']), 1)

    def test_2(self):
        self.assertEqual(count_handshakes(['Alice', 'Bob', 'Carol']), 3)

    def test_3(self):
        self.assertEqual(count_handshakes(['Alice', 'Bob', 'Carol', 'David']), 6)


if __name__ == "__main__":
    unittest.main()