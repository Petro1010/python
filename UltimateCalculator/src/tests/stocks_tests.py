import os
import sys
fpath = os.path.join(os.path.dirname(__file__), '../uis/Calculators')
sys.path.append(fpath)
from stocks_calculator import calcUserGainLossCase1, calcUserGainLossCase2

#from tokenize import Double
import unittest

class StockTest(unittest.TestCase):
    
    def test_case1_1(self):
        self.assertEqual(calcUserGainLossCase1(2, 2, 2, 2, 2), -4)
    
    def test_case1_2(self):
        self.assertEqual(calcUserGainLossCase1(0, 0, 0, 0, 0), 0)
    
    def test_case2_1(self):
        self.assertEqual(calcUserGainLossCase2(2, 2, 2), 0)
    
    def test_case2_2(self):
        self.assertEqual(calcUserGainLossCase2(2, 1, 2), 2)

    def test_stock_error(self):
        with self.assertRaises(ValueError):
            calcUserGainLossCase1('hello', 2, 2, 2, 2)

    def test_stock_error_2(self):
        with self.assertRaises(ValueError):
            calcUserGainLossCase1(2, 'hello', 2, 2, 2)

    def test_stock_error_3(self):
        with self.assertRaises(ValueError):
            calcUserGainLossCase1(2, 2, 'hello', 2, 2)

    def test_stock_error_4(self):
        with self.assertRaises(ValueError):
            calcUserGainLossCase1(2, 2, 2, 'hello', 2)

    def test_stock_error_5(self):
        with self.assertRaises(ValueError):
            calcUserGainLossCase1(2, 2, 2, 2, 'hello')

    def test_stock_error_6(self):
        with self.assertRaises(ValueError):
            calcUserGainLossCase2('hello', 2, 2)

    def test_stock_error_7(self):
        with self.assertRaises(ValueError):
            calcUserGainLossCase2(2, 'hello', 2)

    def test_stock_error_8(self):
        with self.assertRaises(ValueError):
            calcUserGainLossCase2(2, 2, 'hello')
    
if __name__ == "__main__":
    unittest.main()