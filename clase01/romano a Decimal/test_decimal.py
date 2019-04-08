import unittest
from decimal_numbers import decimal_to_roman

class TestDecimalNumbers(unittest.TestCase):
    def test_decimal_1_to_roman(self):
        roman_number = decimal_to_roman (1)
        self.assertEqual(roman_number,'I')
    def test_decimal_2_to_roman(self):
        roman_number = decimal_to_roman (2)
        self.assertEqual(roman_number,'II')
    def test_decimal_3_to_roman(self):
        roman_number = decimal_to_roman (3)
        self.assertEqual(roman_number,'III')
    def test_decimal_4_to_roman(self):
        roman_number = decimal_to_roman (4)
        self.assertEqual(roman_number,'IV')
    def test_decimal_5_to_roman(self):
        roman_number = decimal_to_roman (5)
        self.assertEqual(roman_number,'V')
    def test_decimal_6_to_roman(self):
        roman_number = decimal_to_roman (6)
        self.assertEqual(roman_number,'VI')
    def test_decimal_7_to_roman(self):
        roman_number = decimal_to_roman (7)
        self.assertEqual(roman_number,'VII')
    def test_decimal_8_to_roman(self):
        roman_number = decimal_to_roman (8)
        self.assertEqual(roman_number,'VIII')
    def test_decimal_9_to_roman(self):
        roman_number = decimal_to_roman (9)
        self.assertEqual(roman_number,'IX')    
if __name__ == '__main__':
   unittest.main()