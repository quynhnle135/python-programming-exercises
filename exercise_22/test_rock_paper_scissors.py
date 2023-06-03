from rock_paper_scissors import rpsWinner
import unittest


class TestRockPaperScissors(unittest.TestCase):
    def test_rock_paper_scissors_1(self):
        self.assertEqual(rpsWinner("rock", "paper"), "player 2")

    def test_rock_paper_scissors_2(self):
        self.assertEqual(rpsWinner("paper", "rock"), "player 1")

    def test_rock_paper_scissors_3(self):
        self.assertEqual(rpsWinner("scissors", "scissors"), "tie")


if __name__ == "__main__":
    unittest.main()

