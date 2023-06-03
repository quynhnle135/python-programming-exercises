from password_generator import generatePassword, LOWERCASE, UPPERCASE, NUMBER, SPECIAL
import unittest

class TestPasswordGenerator(unittest.TestCase):
    def test_password_generator_1(self):
        self.assertEqual(len(generatePassword(8)), 12)

    def test_password_generate_2(self):
        pw = generatePassword(14)
        hasLowercase = False
        hasUpperCase = False
        hasNumber = False
        hasSpecialChar = False
        for w in pw:
            if w in LOWERCASE:
                hasLowercase = True
            if w in UPPERCASE:
                hasUpperCase = True
            if w in NUMBER:
                hasNumber = True
            if w in SPECIAL:
                hasSpecialChar = True

        self.assertEqual(len(pw), 14)
        self.assertEqual(hasLowercase, True)
        self.assertEqual(hasUpperCase, True)
        self.assertEqual(hasNumber, True)
        self.assertEqual(hasSpecialChar, True)


if __name__ == "__main__":
    unittest.main()