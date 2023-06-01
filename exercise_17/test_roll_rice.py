from roll_dice import roll_dice
import unittest


class TestRollDice(unittest.TestCase):
    def test_roll_dice(self):
        self.assertEqual(roll_dice(0), 0)

    def test_roll_dice_1(self):
        self.assertEqual(1 <= roll_dice(1) <= 6, True)

    def test_roll_dice_2(self):
        self.assertEqual(1 <= roll_dice(2) <= 12, True)

    def test_roll_dice_3(self):
        self.assertEqual(1 <= roll_dice(3) <= 18, True)


if __name__ == "__main__":
    unittest.main()

