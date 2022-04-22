import os
import sys
fpath = os.path.join(os.path.dirname(__file__), '../uis/Calculators')
sys.path.append(fpath)
from geometry_calculator import getArea, getPerimeter, getVolume

import unittest

class GeometryTest(unittest.TestCase):
    def test_getArea_sq(self):
        self.assertEqual(getArea(0,3,None,None,None), 9)

    def test_getArea_rect(self):
        self.assertEqual(getArea(1,3,4,None,None), 12)
    
    def test_getArea_tri(self):
        self.assertEqual(getArea(2,3,4,5,None), 6)

    def test_getArea_cir(self):
        self.assertAlmostEqual(float(getArea(3,None,None,None,2)), 12.5663706144)

    def test_getArea_err1(self):
        with self.assertRaises(ValueError):
            getArea(0,-2,None,None,None)
    
    def test_getArea_err2(self):
        with self.assertRaises(ValueError):
            getArea(0,0,None,None,None)

    def test_getArea_err3(self):
        with self.assertRaises(ValueError):
            getArea(2,0,0,0,None)

    def test_getArea_err4(self):
        with self.assertRaises(ValueError):
            getArea(2,2,2,5,None)
    
    def test_getPerimeter_sq(self):
        self.assertEqual(getPerimeter(0,3,None,None,None), 12)

    def test_getPerimeter_rect(self):
        self.assertEqual(getPerimeter(1,3,4,None,None), 14)
    
    def test_getPerimeter_tri(self):
        self.assertEqual(getPerimeter(2,3,4,5,None), 12)

    def test_getPerimeter_cir(self):
        self.assertAlmostEqual(float(getPerimeter(3,None,None,None,2)), 12.5663706144)

    def test_getPerimeter_err1(self):
        with self.assertRaises(ValueError):
            getPerimeter(0,-2,None,None,None)
    
    def test_getPerimeter_err2(self):
        with self.assertRaises(ValueError):
            getPerimeter(0,0,None,None,None)

    def test_getPerimeter_err3(self):
        with self.assertRaises(ValueError):
            getPerimeter(2,0,0,0,None)

    def test_getPerimeter_err4(self):
        with self.assertRaises(ValueError):
            getPerimeter(2,2,2,5,None)

    def test_getVolume_cb(self):
        self.assertEqual(getVolume(0,3,None,None,None), 27)

    def test_getVolume_rectp(self):
        self.assertEqual(getVolume(1,3,4,2,None), 24)
    
    def test_getVolume_cyl(self):
        self.assertAlmostEqual(float(getVolume(2,None,None,5,2)), 62.8318530718)

    def test_getVolume_sph(self):
        self.assertAlmostEqual(float(getVolume(3,None,None,None,2)), 33.5103216383)

    def test_getVolume_err1(self):
        with self.assertRaises(ValueError):
            getVolume(0,-2,None,None,None)
    
    def test_getVerimeter_err2(self):
        with self.assertRaises(ValueError):
            getVolume(0,0,None,None,None)

    def test_getVolume_err3(self):
        with self.assertRaises(ValueError):
            getVolume(2,0,0,0,None)

if __name__ == "__main__":
    unittest.main()