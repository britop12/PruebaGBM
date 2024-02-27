import unittest
from solucion import isPalindrome

class TestEsPalindromo(unittest.TestCase):

    def test_esPalindromo(self):
        self.assertTrue(isPalindrome("ANA"))
        self.assertTrue(isPalindrome("Ana"))

    def test_noEsPalindromo(self):
        self.assertFalse(isPalindrome("Anita"))
        self.assertFalse(isPalindrome("anita"))
    
    def test_esPalindromoConEspacios(self):
        self.assertTrue(isPalindrome("Anita lava la tina"))
        self.assertTrue(isPalindrome("Anita lava la tina"))

if __name__ == '__main__':
    # logs = open("output.txt", "w")
    unittest.main(verbosity=2)
    # runner = unittest.TextTestRunner(logs, verbosity=2)
    # unittest.main(testRunner=runner)