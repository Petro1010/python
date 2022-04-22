import os
import sys
fpath = os.path.join(os.path.dirname(__file__), '../uis/Calculators')
sys.path.append(fpath)
from binary_calculator import toFloatingPoint, toDecimal, binAdd, binSub, binMult, binDiv, binPow, bitwiseAND, bitwiseOR, bitwiseNOT, bitwiseXOR, rshift, lshift

import unittest

class BinaryTest(unittest.TestCase):
    def test_toFloatingPoint(self):
        self.assertEqual(toFloatingPoint(104.2), "0100000001011010000011001100110011001100110011001100110011001101")

    def test_toDecimal(self):
        self.assertEqual(toDecimal("0100000000110111111001100110011001100110011001100110011001100110"), "23.9")

    def test_binAdd(self):
        self.assertEqual(binAdd(int("1010",2), int("1101",2)), "10111")

    def test_binSub(self):
        self.assertEqual(binSub(int("1110",2), int("1001",2)), "101")
    
    def test_binMult(self):
        self.assertEqual(binMult(int("1110",2), int("1001",2)), "1111110")

    def test_binDiv(self):
        self.assertEqual(binDiv(int("1110",2), int("1001",2)), "10")

    def test_binDiv_ZeroDivisionError(self):
        with self.assertRaises(ZeroDivisionError):
            binDiv(int("1001",2), int("0",2))

    def test_binPow(self):
        self.assertEqual(binPow(int("1110",2), int("1001",2)), "10011001111011111101000111000000000")

    def test_bitwiseAND(self):
        self.assertEqual(bitwiseAND(int("10101", 2), int("11001",2)), "10001")

    def test_bitwiseOR(self):
        self.assertEqual(bitwiseOR(int("10101", 2), int("11001",2)), "11101")

    def test_bitwiseNOT(self):
        self.assertEqual(bitwiseNOT(int("10101", 2)), "01010")

    def test_bitwiseXOR(self):
        self.assertEqual(bitwiseXOR(int("10101", 2), int("11001",2)), "1100")

    def test_rshift(self):
        self.assertEqual(rshift(int("10101", 2), 2, 5), "00101")

    def test_rshift_nGreaterThanLength(self):
        with self.assertRaises(ValueError):
            rshift(int("1001",2), 2, 2)

    def test_lshift(self):
        self.assertEqual(lshift(int("10101", 2), 2, 7), "1010100")

    def test_lshift_nGreaterThanLength(self):
        with self.assertRaises(ValueError):
            lshift(int("1001",2), 2, 2)

if __name__ == "__main__":
    unittest.main()