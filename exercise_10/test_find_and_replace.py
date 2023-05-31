import unittest
from find_and_replace import find_and_replace_advanced, find_and_replace


class TestFindAndReplace(unittest.TestCase):
    def test_find_and_replace_1(self):
        self.assertEqual(find_and_replace("the fox", "fox", "dog"), "the dog")

    def test_find_and_replace_2(self):
        self.assertEqual(find_and_replace("Firefox", "fox", "dog"), "Firedog")

    def test_find_and_replace_3(self):
        self.assertEqual(find_and_replace("one two three", "two", "ten"), "one ten three")

    def test_find_and_replace_advanced_1(self):
        self.assertEqual(find_and_replace_advanced("the fox", "fox", "dog"), "the dog")

    def test_find_and_replace_advanced_2(self):
        self.assertEqual(find_and_replace_advanced("Firefox", "fox", "dog"), "Firedog")

    def test_find_and_replace_advanced_3(self):
        self.assertEqual(find_and_replace_advanced("one two three", "two", "ten"), "one ten three")


if __name__ == "__main__":
    unittest.main()
