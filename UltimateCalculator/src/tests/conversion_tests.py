import os
import sys
fpath = os.path.join(os.path.dirname(__file__), '../uis/Calculators')
sys.path.append(fpath)
from conversion_calculator import convertCurrency, convertCrypto, convertBase, convertRN
import unittest

class ConversionTest(unittest.TestCase):

    def test_convert_currency_1(self):
        self.assertEqual(float(convertCurrency("10", "US Dollars", "Euros")), 9.1)

    def test_convert_currency_2(self):
        self.assertAlmostEqual(float(convertCurrency("25.5", "US Dollars", "Euros")), 23.2050, 4)

    def test_convert_currency_3(self):
        self.assertAlmostEqual(float(convertCurrency("231.4", "Jap Yen", "CA Dollars")), 2.5454, 4)
    
    def test_convert_crypto_1(self):
        self.assertAlmostEqual(float(convertCrypto("123.45", "Bitcoin", "Ethereum")), 1733.2379999999998, 4)

    def test_convert_crypto_2(self):
        self.assertAlmostEqual(float(convertCrypto("76543.21", "Ethereum", "Dogecoin")), 1874035731.4177, 4)

    def test_convert_crypto_3(self):
        self.assertAlmostEqual(float(convertCrypto("321321.321", "Ethereum", "Bitcoin")),22813.81379, 4)


    def test_convert_base_1(self):
        self.assertEqual((convertBase("12345", "10", "2")),"01100000011100")

    def test_convert_base_2(self):
        self.assertEqual((convertBase("12345", "10", "8")),"30071")

    def test_convert_base_3(self):
        self.assertEqual((convertBase("12345", "10", "16")),"3039")


    def test_convert_RN_1(self):
        self.assertEqual((convertRN("12345", "Decimal", "Roman Numerals")),"MMMMMMMMMMMMCCCXLV")

    def test_convert_RN_2(self):
        self.assertEqual((convertRN("MMCCXLV", "Roman Numerals", "Decimal")), 2245)

    
if __name__ == "__main__":
    unittest.main()