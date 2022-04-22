import os
import sys
fpath = os.path.join(os.path.dirname(__file__), '../uis/Calculators')
sys.path.append(fpath)
from gpa_calculator import gpaCalculate

#from tokenize import Double
import unittest

class GPATest(unittest.TestCase):
    
    def test_gpaCalculate_1(self):
        self.assertEqual(gpaCalculate([20,27,40,28,15], 16),'8.125')

    def test_gpaCalculate_2(self):
        self.assertEqual(gpaCalculate([0,0,0,0,0], 10),'0.0')

    def test_gpaCalculate_3(self):
        self.assertEqual(gpaCalculate([10,10,10,10,10], 10),'5.0')

    def test_gpaCalculate_error(self):
        with self.assertRaises(ZeroDivisionError):
            gpaCalculate([20,27,40,28,15], 0)

    def test_gpaCalculate_error_2(self):
        with self.assertRaises(ZeroDivisionError):
            gpaCalculate([0,0,0,0,0], 0)

if __name__ == "__main__":
    unittest.main()