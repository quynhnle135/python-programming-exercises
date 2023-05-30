import unittest
from chess_square_color import get_chess_square_color


class TestChessSquareColor(unittest.TestCase):
    def test_get_chess_square_color_1(self):
        self.assertEqual(get_chess_square_color(1, 1), "white")

    def test_get_chess_square_color_2(self):
        self.assertEqual(get_chess_square_color(2, 1), "black")

    def test_get_chess_square_color_3(self):
        self.assertEqual(get_chess_square_color(1, 2), "black")

    def test_get_chess_square_color_4(self):
        self.assertEqual(get_chess_square_color(8, 8), "white")

    def test_get_chess_square_color_5(self):
        self.assertEqual(get_chess_square_color(0, 8), "")

    def test_get_chess_square_color_6(self):
        self.assertEqual(get_chess_square_color(2, 9), "")


if __name__ == "__main__":
    unittest.main
