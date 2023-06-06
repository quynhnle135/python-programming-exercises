from uppercase_letters import get_upper_case
import unittest


class TestUpperCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(get_upper_case("Hello"), "HELLO")

    def test_2(self):
        self.assertEqual(get_upper_case("hello"), "HELLO")

    def test_3(self):
        self.assertEqual(get_upper_case("HELLO"), "HELLO")

    def test_4(self):
        self.assertEqual(get_upper_case("Hello, world!"), "HELLO, WORLD!")

    def test_5(self):
        self.assertEqual(get_upper_case("goodbye, 123"), "GOODBYE, 123")

    def test_6(self):
        self.assertEqual(get_upper_case("12345"), "12345")

    def test_7(self):
        self.assertEqual(get_upper_case(""), "")


if __name__ == "__main__":
    unittest.main()