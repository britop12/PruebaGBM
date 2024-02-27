import unittest
from solucion import findChampions

class TestEsPalindromo(unittest.TestCase):

    def test_firstSample(self):
        firstCase = """
        1 3
        3 2 1
        3
        3 5 3 2
        3 5 3 1
        3 1 1 1"""

        expected = "3\n3\n1 2 3"

        self.assertEqual(findChampions(firstCase), expected)
    
    def test_secondSample(self):
        secondCase = """3 10
        1 2 3 4 5 6 7 8 9 10
        10 1 2 3 4 5 6 7 8 9
        9 10 1 2 3 4 5 6 7 8
        2
        5 5 4 3 2 1
        3 10 5 1"""

        expected = "3\n3"

        self.assertEqual(findChampions(secondCase), expected)

    def test_thirdSample(self):
        thirdCase = """2 4
        1 3 4 2
        4 1 3 2
        2
        3 3 2 1
        3 5 4 2"""

        expected = "2 4\n4"

        self.assertEqual(findChampions(thirdCase), expected)

    def test_fourthSample(self):
        fourthCase = """0 0"""

        expected = ""

        self.assertEqual(findChampions(fourthCase), expected)

    def test_fifthSample(self):
        fifthCase = """3 2
        1 2
        2 1
        1 2
        3
        2 3 1
        2 1 3
        3 1 1"""

        # Hay 3 carreras, 2 pilotos
        # Hay 3 sistemas de puntuación
        # El primer sistema da al primero 3 puntos, al segundo 1
        # El segundo sistema da al primero 1 punto, al segundo 3 (El que queda siempre de último en las carrera gana)
        # El tercer sistema da a ambos 1 punto (Por lo tanto siempre empatan)


        expected = "1\n2\n1 2"

        self.assertEqual(findChampions(fifthCase), expected)



if __name__ == '__main__':
    # logs = open("output.txt", "w")
    unittest.main(verbosity=2)
    # runner = unittest.TextTestRunner(logs, verbosity=2)
    # unittest.main(testRunner=runner)