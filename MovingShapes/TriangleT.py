## @file TriangleT.py
#  @author Mathew Petronilho
#  @brief Provides the TriangleT ADT class for representing triangles
#  @date February 2, 2021


from Shape import *

## @brief TriangleT is a class that implements an ADT for a triangle
#  @details An equliateral triangle is defined by its mass, the coordinates of its
#  center of mass, and its side length


class TriangleT(Shape):

    ## @brief TriangleT constructor
    #  @details Creates an equilateral triangle shape based on the given mass, center of mass
    #  coordinates and side length. We assume the parameters will be of the correct type.
    #  @param x real number that represents the x coordinate of the center of mass
    #  @param y real number that represents the y coordinate of the center of mass
    #  @param s real number that represents the side length of the triangle
    #  @param m real number that represents the mass of the triangle
    #  @throws ValueError Throws an exception if s or m is not greater than zero
    def __init__(self, x, y, s, m):
        if not(s > 0 and m > 0):
            raise ValueError

        self.x = x
        self.y = y
        self.s = s
        self.m = m

    ## @brief Gets the x coordinate of the center of mass of the triangle
    #  @return A real number that represents the x coordinate of the center of mass
    def cm_x(self):
        return self.x

    ## @brief Gets the y coordinate of the center of mass of the triangle
    #  @return A real number that represents the y coordinate of the center of mass
    def cm_y(self):
        return self.y

    ## @brief Gets the mass of the triangle
    #  @return A real number that represents the mass
    def mass(self):
        return self.m

    ## @brief Gets the moment of inertia of the triangle
    #  @return A real number that represents the moment of inertia
    def m_inert(self):
        return (self.m * (self.s)**2) / 12
