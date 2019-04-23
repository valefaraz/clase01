import unittest
from vigenere import vigenere

class TestVigenere(unittest.TestCase):
    def test_vigenere_1(self):
        result = vigenere ('WIKIHOWISTHEBEST','LIMELIMELIMELIME')
        self.assertEqual(result, 'HPVMRWIMDBSIMMEX')

    def test_vigenere_2(self):
        result = vigenere ('VALENTIN','FARAZ')
        self.assertEqual(result, 'AACEMYIE')

if __name__ == '__main__':
    unittest.main()
