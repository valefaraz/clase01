import unittest
from ronam_numbers import roman_to_decimal

class TestRomanNumbers(unittest.TestCase):
    def test_roman_I_to_decimal(self):
        decimal_number = roman_to_decimal('I')
        self.assertEqual(decimal_number, 1)
    
    def test_roman_II_to_decimal(self):
        decimal_number = roman_to_decimal('II')
        self.assertEqual(decimal_number, 2)

    def test_roman_III_to_decimal(self):
        decimal_number = roman_to_decimal('III')
        self.assertEqual(decimal_number, 3)

    def test_roman_IV_to_decimal(self):
        decimal_number = roman_to_decimal('IV')
        self.assertEqual(decimal_number, 4)


    def test_roman_V_to_decimal(self):
        decimal_number = roman_to_decimal('V')
        self.assertEqual(decimal_number, 5)

    def test_roman_VI_to_decimal(self):
        decimal_number = roman_to_decimal('VI')
        self.assertEqual(decimal_number, 6)

    def test_roman_VII_to_decimal(self):
        decimal_number = roman_to_decimal('VII')
        self.assertEqual(decimal_number, 7)

    def test_roman_VIII_to_decimal(self):
        decimal_number = roman_to_decimal('VIII')
        self.assertEqual(decimal_number, 8)

    def test_roman_IX_to_decimal(self):
        decimal_number = roman_to_decimal('IX')
        self.assertEqual(decimal_number, 9)

    def test_roman_X_to_decimal(self):
        decimal_number = roman_to_decimal('X')
        self.assertEqual(decimal_number, 10)
    
    def test_roman_XI_to_decimal(self):
        decimal_number = roman_to_decimal('XI')
        self.assertEqual(decimal_number, 11)

    def test_roman_XII_to_decimal(self):
        decimal_number = roman_to_decimal('XII')
        self.assertEqual(decimal_number, 12)

    def test_roman_XIII_to_decimal(self):
        decimal_number = roman_to_decimal('XIII')
        self.assertEqual(decimal_number, 13)

    def test_roman_XV_to_decimal(self):
        decimal_number = roman_to_decimal('XV')
        self.assertEqual(decimal_number, 15)

    def test_roman_XXIV_to_decimal(self):
        decimal_number = roman_to_decimal('XXIV')
        self.assertEqual(decimal_number, 24)

    def test_roman_XLIII_to_decimal(self):
        decimal_number = roman_to_decimal('XLIII')
        self.assertEqual(decimal_number, 43)

    def test_roman_L_to_decimal(self):
        decimal_number = roman_to_decimal('L')
        self.assertEqual(decimal_number, 50)

    def test_roman_C_to_decimal(self):
        decimal_number = roman_to_decimal('C')
        self.assertEqual(decimal_number, 100)

if __name__== '__main__':
    unittest.main() 