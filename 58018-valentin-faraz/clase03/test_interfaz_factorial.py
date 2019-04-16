import unittest
from interfaz_factorial import interfaz_factorial


class TestInterfazFactorial(unittest.TestCase):
    def test_interfaz_factorial_5(self):
       
       result=interfaz_factorial('5')

       self.assertEqual(result, 120)

    def test_interfaz_factorial_hola(self):

        result=interfaz_factorial('hola')

        self.assertEqual(result,'Error')

    def test_interfaz_factorial_(self):
    
        result=interfaz_factorial('')

        self.assertEqual(result,'Error')

    
       
if __name__ == '__main__':
   unittest.main()
