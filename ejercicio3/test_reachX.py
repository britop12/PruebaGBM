import unittest
from solucion3 import reachX

class TestreachX(unittest.TestCase):

    def test_firstSample(self):
        firstCase = "5\n1\n2\n3\n4\n5"
        expected = "1\n3\n2\n3\n4"
        self.assertEqual(reachX(firstCase), expected)

    def test_secondSample(self):
        secondCase = "10\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10"
        expected = "1\n3\n2\n3\n4\n3\n4\n4\n5\n4"
        self.assertEqual(reachX(secondCase), expected)

    def test_thirdSample(self):
        thirdCase = "1\n1"
        expected = "1"
        self.assertEqual(reachX(thirdCase), expected)

    def test_fourthSample(self):
        fourthCase = "1\n2"
        expected = "3"
        self.assertEqual(reachX(fourthCase), expected)
    
    def test_fifthSample(self):
        fifthCase = "1\n3"
        expected = "2"
        self.assertEqual(reachX(fifthCase), expected)



if __name__ == '__main__':
    # logs = open("output.txt", "w")
    unittest.main(verbosity=2)
    # runner = unittest.TextTestRunner(logs, verbosity=2)
    # unittest.main(testRunner=runner)