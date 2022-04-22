import os
import sys
fpath = os.path.join(os.path.dirname(__file__), '../uis/Calculators')
sys.path.append(fpath)
from algebra_calculator import slopeOfLine, yIntercept, pyTheorem
import unittest

class AlgebraTest(unittest.TestCase):
    def test_slope_1(self):
        self.assertEqual(float(slopeOfLine(5, 4, 6, 4)), 0)
    
    def test_slope_2(self):
        self.assertEqual(float(slopeOfLine(0, 4, 4, 8)), 1)

    def test_slope_3(self):
        self.assertEqual(float(slopeOfLine(-1, -1, -5, -5)), 1)
    
    def test_slope_4(self):
        self.assertEqual(float(slopeOfLine(5, -1, 3, 3)), -2)
    
    def test_slope_5(self):
        with self.assertRaises(ZeroDivisionError):
            slopeOfLine(9, 8, 9, -2)
    
    def test_slope_6(self):
        with self.assertRaises(ZeroDivisionError):
            slopeOfLine(0, 0, 0, 0)
    
    def test_slope_6(self):
        with self.assertRaises(ZeroDivisionError):
            slopeOfLine(0, 0, 0, 0)
    
    def test_slope_7(self):
        self.assertEqual(float(slopeOfLine(1000000000, 2000000000, 500000000, 1000000000)), 2)
    
    def test_y_1(self):
        self.assertEqual(float(yIntercept(0.0, 0, 0)), 0)
    
    def test_y_2(self):
        self.assertEqual(float(yIntercept(3.0, 1, 4)), 1)
    
    def test_y_3(self):
        self.assertEqual(float(yIntercept(-3.0, -1, -4)), -7)
    
    def test_y_4(self):
        self.assertEqual(float(yIntercept(2.0, -3, 5)), 11)
    
    def test_y_5(self):
        self.assertEqual(float(yIntercept(100000000000.0, 600000, -40000000000)), -6.000004e16)
    
    def test_py_1(self):
        self.assertEqual(float(pyTheorem("A", None, 3, 5)), 4)
    
    def test_py_2(self):
        self.assertEqual(float(pyTheorem("B", 3, None, 5)), 4)
    
    def test_py_3(self):
        self.assertEqual(float(pyTheorem("C", 3, 4, None)), 5)
    
    def test_py_4(self):
        with self.assertRaises(ValueError):
            pyTheorem("A", None, 4, 1)
    
    def test_py_5(self):
        with self.assertRaises(ValueError):
            pyTheorem("A", None, -4, -1)
    
    def test_py_6(self):
        self.assertEqual(float(pyTheorem("C", 3000000000000000, 4000000000000000, None)), 5000000000000000)
    
if __name__ == "__main__":
    unittest.main()