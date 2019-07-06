import unittest
from two_fer import two_fer

class TwoFerTest(unittest.TestCase):
    def test_no_name_provided(self):
        self.assertEqual(two_fer(),'One for you, one for me.')
    
    def test_a_given_name(self):
        self.assertEqual(two_fer('Alice'),'One for Alice, one for me.')

    def test_a_given_another_name(self):
        self.assertEqual(two_fer('John'),'One for John, one for me.')

if __name__ == "__main__":
    unittest.main()
