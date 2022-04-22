## @file geometry_calculator.py
#  @brief Geometry algorithms
#  @date March 18, 2022

import math

## @brief Calculates area of given shape with given side lengths or radius
#  @param shape An integer that represents the shape
#  @param a Side length a
#  @param b Side length b
#  @param c Side length c
#  @param r Radius
#  @return Area
#  @throws ValueError Throws an exception if required side lengths or radius are invalid
from unittest.loader import VALID_MODULE_NAME


def getArea(shape, a, b, c, r):
    #shape 0: square
    #shape 1: rectangle
    #shape 2: triangle
    #shape 3: circle

    if shape == 0:
        if a <= 0:
            raise ValueError
        return a**2
    elif shape == 1:
        if a <= 0 or b <= 0:
            raise ValueError
        return a*b
    elif shape == 2:
        sides = sorted([a,b,c])
        if a <= 0 or b <= 0 or c <= 0 or sides[2] >= sides[0] + sides[1]:
            raise ValueError
        s = (a + b + c) / 2
        return (s*(s-a)*(s-b)*(s-c))**0.5
    elif shape == 3:
        if r <= 0:
            raise ValueError
        return format(math.pi*r**2, ".13")
        
## @brief Calculates perimeter of given shape with given side lengths or radius
#  @param shape An integer that represents the shape
#  @param a Side length a
#  @param b Side length b
#  @param c Side length c
#  @param r Radius
#  @return Perimeter
#  @throws ValueError Throws an exception if required side lengths or radius are invalid
def getPerimeter(shape, a, b, c, r):
    if shape == 0:
        if a <= 0:
            raise ValueError
        return 4*a
    elif shape == 1:
        if a <= 0 or b <= 0:
            raise ValueError
        return 2*a + 2*b
    elif shape == 2:
        sides = sorted([a,b,c])
        if a <= 0 or b <= 0 or c <= 0 or sides[2] >= sides[0] + sides[1]:
            raise ValueError
        return a + b + c
    elif shape == 3:
        if r <= 0:
            raise ValueError
        return format(2*math.pi*r,".13")

## @brief Calculates volume of given shape with given dimensions
#  @param shape An integer that represents the shape
#  @param l Length
#  @param w Width
#  @param h Height
#  @param r Radius
#  @return Volume
#  @throws ValueError Throws an exception if required dimensions invalid
def getVolume(shape, l, w, h, r):
    #shape 0: cube
    #shape 1: rectangular prism
    #shape 2: cylinder
    #shape 3: sphere
   
    if shape == 0:
        if l <= 0:
            raise ValueError
        return l**3
    elif shape == 1:
        if l <= 0 or w <= 0 or h <= 0:
            raise ValueError
        return l*w*h
    elif shape == 2:
        if h <= 0 or r <= 0:
            raise ValueError
        return h*math.pi*r**2
    elif shape == 3:
        if r <= 0:
            raise ValueError
        return format(4/3*math.pi*r**3, ".13")
