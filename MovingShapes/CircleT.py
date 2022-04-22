## @file CircleT.py
#  @author Mathew Petronilho
#  @brief Provides the CircleT ADT class for representing circles
#  @date February 2, 2021


from Shape import *

## @brief CircleT is a class that implements an ADT for a circle
#  @details A circle is defined by its mass, the coordinates of its
#  center of mass, and its radius


class CircleT(Shape):

    ## @brief CircleT constructor
    #  @details Creates a circle shape based on the given mass, center of mass
    #  coordinates and radius. We assume the parameters will be of the correct type.
    #  @param x real number that represents the x coordinate of the center of mass
    #  @param y real number that represents the y coordinate of the center of mass
    #  @param r real number that represents the radius of the circle
    #  @param m real number that represents the mass of the circle
    #  @throws ValueError Throws an exception if r or m is not greater than zero
    def __init__(self, x, y, r, m):
        if not(r > 0 and m > 0):
            raise ValueError

        self.x = x
        self.y = y
        self.r = r
        self.m = m

    ## @brief Gets the x coordinate of the center of mass of the circle
    #  @return A real number that represents the x coordinate of the center of mass
    def cm_x(self):
        return self.x

    ## @brief Gets the y coordinate of the center of mass of the circle
    #  @return A real number that represents the y coordinate of the center of mass
    def cm_y(self):
        return self.y

    ## @brief Gets the mass of the circle
    #  @return A real number that represents the mass
    def mass(self):
        return self.m

    ## @brief Gets the moment of inertia of the circle
    #  @return A real number that represents the moment of inertia
    def m_inert(self):
        return (self.m * (self.r)**2) / 2
