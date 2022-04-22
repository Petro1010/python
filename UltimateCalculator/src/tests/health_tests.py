import os
import sys
fpath = os.path.join(os.path.dirname(__file__), '../uis/Calculators')
sys.path.append(fpath)
from health_calculator import bodyMassIndex, bodyFat

#from tokenize import Double
import unittest

class HealthTest(unittest.TestCase):
    def setUp(self):
        self.bmi_message1 = "Indicates Severe Thinness"
        self.bmi_message2 = "Indicates Moderate Thinness"
        self.bmi_message3 = "Indicates Mild Thinness"
        self.bmi_message4 = "Indicates Normal Weight"
        self.bmi_message5 = "Indicates Overweight"
        self.bmi_message6 = "Indicates Mild Obesity"
        self.bmi_message7 = "Indicates Moderate Obesity"
        self.bmi_message8 = "Indicates Severe Obesity"

        self.bf_message1 = "Indicates Less than Essential Fat"
        self.bf_message2 = "Indicates Essential Fat"
        self.bf_message3 = "Indicates you are an Athlete"
        self.bf_message4 = "Indicates you are Fit"
        self.bf_message5 = "Indicates Average Fat"
        self.bf_message6 = "Indicates Obesity"


    
    def test_bmi_1(self):
        bmi, message = bodyMassIndex(140, 70)
        self.assertEqual(message, self.bmi_message4)
        self.assertAlmostEqual(float(bmi), 20.086, places=3)
    
    def test_bmi_2(self):
        bmi, message = bodyMassIndex(140, 75)
        self.assertEqual(message, self.bmi_message3)
        self.assertAlmostEqual(float(bmi), 17.497, places=3)
    
    def test_bmi_3(self):
        bmi, message = bodyMassIndex(130, 75)
        self.assertEqual(message, self.bmi_message2)
        self.assertAlmostEqual(float(bmi), 16.247, places=3)
    
    def test_bmi_4(self):
        bmi, message = bodyMassIndex(120, 75)
        self.assertEqual(message, self.bmi_message1)
        self.assertAlmostEqual(float(bmi), 14.997, places=3)
    
    def test_bmi_5(self):
        bmi, message = bodyMassIndex(180, 70)
        self.assertEqual(message, self.bmi_message5)
        self.assertAlmostEqual(float(bmi), 25.824, places=3)
    
    def test_bmi_6(self):
        bmi, message = bodyMassIndex(220, 70)
        self.assertEqual(message, self.bmi_message6)
        self.assertAlmostEqual(float(bmi), 31.563, places=3)
    
    def test_bmi_7(self):
        bmi, message = bodyMassIndex(250, 70)
        self.assertEqual(message, self.bmi_message7)
        self.assertAlmostEqual(float(bmi), 35.867, places=3)
    
    def test_bmi_8(self):
        bmi, message = bodyMassIndex(300, 70)
        self.assertEqual(message, self.bmi_message8)
        self.assertAlmostEqual(float(bmi), 43.041, places=3)
    
    def test_bmi_9(self):
        with self.assertRaises(ZeroDivisionError):
            bodyMassIndex(0, 0)
    
    def test_bmi_10(self):
        with self.assertRaises(ValueError):
            bodyMassIndex(8, -300002)
    
    def test_bmi_11(self):
        with self.assertRaises(ValueError):
            bodyMassIndex(-8, 300002)
    
    def test_bmi_12(self):
        bmi, message = bodyMassIndex(3000000000, 70000000000)
        self.assertEqual(message, self.bmi_message1)
        self.assertAlmostEqual(float(bmi), 4.304e-10, places=3)
    
    def test_bf_1(self):
        bf, message = bodyFat(140, 70, "Male", 20)
        self.assertEqual(message, self.bf_message3)
        self.assertAlmostEqual(float(bf), 12.5, places=1)
    
    def test_bf_2(self):
        bf, message = bodyFat(140, 70, "Female", 20)
        self.assertEqual(message, self.bf_message4)
        self.assertAlmostEqual(float(bf), 23.3, places=1)
    
    def test_bf_3(self):
        bf, message = bodyFat(90, 70, "Male", 20)
        self.assertEqual(message, self.bf_message2)
        self.assertAlmostEqual(float(bf), 3.9, places=1)
    
    def test_bf_4(self):
        bf, message = bodyFat(30, 82, "Female", 50)
        self.assertEqual(message, self.bf_message1)
        self.assertAlmostEqual(float(bf), 9.9, places=1)
    
    def test_bf_5(self):
        bf, message = bodyFat(140, 70, "Female", 50)
        self.assertEqual(message, self.bf_message5)
        self.assertAlmostEqual(float(bf), 30.2, places=1)
    
    def test_bf_6(self):
        bf, message = bodyFat(180, 70, "Male", 50)
        self.assertEqual(message, self.bf_message6)
        self.assertAlmostEqual(float(bf), 26.3, places=1)
    
    def test_bf_7(self):
        with self.assertRaises(ZeroDivisionError):
            bodyFat(0, 0, "Male", 0)
    
    def test_bf_8(self):
        with self.assertRaises(ValueError):
            bodyFat(-140, 70, "Male", 20)

    def test_bf_9(self):
        with self.assertRaises(ValueError):
            bodyFat(140, -70, "Male", 20)
    
    def test_bf_10(self):
        with self.assertRaises(ValueError):
            bodyFat(140, 70, "Male", -20)
    
    def test_bf_11(self):
        with self.assertRaises(ValueError):
            bodyFat(-140, -70, "Male", -20)
    
    def test_bf_12(self):
        bf, message = bodyFat(180000000000, 70000000000, "Male", 50000000000)
        self.assertEqual(message, self.bf_message6)
        self.assertAlmostEqual(float(bf), 11499999983.8, places=1)
    
if __name__ == "__main__":
    unittest.main()