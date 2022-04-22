import os
import sys
fpath = os.path.join(os.path.dirname(__file__), '../uis/Calculators')
sys.path.append(fpath)
from main_calculator import Calculator

#from tokenize import Double
import unittest

class MainCalcTest(unittest.TestCase):

    Calc1 = Calculator()
    Calc2 = Calculator()
    
    def test_getNum(self):
        self.Calc1.currNum = "3000"
        self.assertEqual(self.Calc1.getCurrNum(), "3000")

    def test_storeMem(self):
        self.Calc1.currNum = "5000"
        self.Calc1.storeMem()
        self.assertEqual(self.Calc1.mem, "5000")

    def test_getMem(self):
        self.Calc2.mem = "7000"
        self.Calc2.getMem()
        self.assertEqual(self.Calc2.currNum, "7000")

    def test_valueInput(self):
        self.Calc1.currNum = "100"
        v = "10"
        self.Calc1.valueInput(v)
        self.assertEqual(self.Calc1.currNum, "10010")

    def test_reset(self):
        self.Calc1.currNum = "100"
        self.Calc1.lineEdit = "1000"
        self.Calc1.reset()
        self.assertEqual(self.Calc1.currNum, "")
        self.assertEqual(self.Calc1.lineEdit, "")

    def test_addition(self):
        self.Calc1.lineEdit = "200"
        self.Calc1.addition()
        self.assertEqual(self.Calc1.currNum, "")
        self.assertEqual(self.Calc1.lineEdit, "200+")

    def test_subtraction(self):
        self.Calc1.lineEdit = "300"
        self.Calc1.subtraction()
        self.assertEqual(self.Calc1.currNum, "")
        self.assertEqual(self.Calc1.lineEdit, "300-")

    def test_power(self):
        self.Calc1.lineEdit = "400"
        self.Calc1.power()
        self.assertEqual(self.Calc1.currNum, "")
        self.assertEqual(self.Calc1.lineEdit, "400**")

    def test_division(self):
        self.Calc1.lineEdit = "500"
        self.Calc1.division()
        self.assertEqual(self.Calc1.currNum, "")
        self.assertEqual(self.Calc1.lineEdit, "500/")

    def test_leftBracket(self):
        self.Calc1.lineEdit = "800"
        self.Calc1.left_bracket()
        self.assertEqual(self.Calc1.currNum, "")
        self.assertEqual(self.Calc1.lineEdit, "800(")

    def test_rightBracket(self):
        self.Calc1.lineEdit = "900"
        self.Calc1.right_bracket()
        self.assertEqual(self.Calc1.currNum, "")
        self.assertEqual(self.Calc1.lineEdit, "900)")

    def test_evaluate(self):
        self.Calc1.lineEdit = "10+1"
        self.Calc1.evaluate()
        self.assertEqual(self.Calc1.lineEdit, "11")
        self.assertEqual(self.Calc1.currNum, "11.0")

    def test_delete(self):
        self.Calc1.lineEdit = "1111"
        self.Calc1.currNum = "1111"
        self.Calc1.delete()
        self.assertEqual(self.Calc1.lineEdit, "111")
        self.assertEqual(self.Calc1.currNum, "111")
    
if __name__ == "__main__":
    unittest.main()