## @file BodyT.py
#  @author Mathew Petronilho
#  @brief Provides the BodyT ADT class for representing an unidentified shape
#  @date February 4, 2021


from Shape import *

## @brief BodyT is a class that implements an ADT for an unidentified shape
#  @details A body is defined by many points of different masses


class BodyT(Shape):

    ## @brief BodyT constructor
    #  @details Creates a body based on the mass and coordinates of all the points
    #  that it is made up of. We assume the parameters will be of the correct type.
    #  @param x a list of real numbers that represents the x coordinates of the center of
    #  masses of the points
    #  @param y a list of real numbers that represents the y coordinates of the center of
    #  masses of the points
    #  @param m a list of real numbers that represents the mass of each point in the body
    #  @throws ValueError Throws an exception if the lists are not the same length or one of
    #  the masses are not greater than zero.
    def __init__(self, x, y, m):
        if not(len(x) == len(y) and len(y) == len(m)):
            raise ValueError
        for u in m:
            if not (u > 0):
                raise ValueError

        self.cmx = self.__cm__(x, m)
        self.cmy = self.__cm__(y, m)
        self.m = self.__sum__(m)
        self.moment = self.__mmom__(x, y, m) - (self.m * (self.cmx**2 + self.cmy**2))

    ## @brief Gets the x coordinate of the center of mass of the body
    #  @return A real number that represents the x coordinate of the center of mass
    def cm_x(self):
        return self.cmx

    ## @brief Gets the y coordinate of the center of mass of the body
    #  @return A real number that represents the y coordinate of the center of mass
    def cm_y(self):
        return self.cmy

    ## @brief Gets the total mass of the body
    #  @return A real number that represents the total mass
    def mass(self):
        return self.m

    ## @brief Gets the moment of inertia of the body
    #  @return A real number that represents the moment of inertia
    def m_inert(self):
        return self.moment

    ## @brief Gets the sum of a sequence of real numbers
    #  @param m Sequence of real numbers that represent masses
    #  @return The total sum of all the numbers in the sequence
    def __sum__(self, m):
        total = 0
        for i in m:
            total += i
        return total

    ## @brief Gets the center of mass of a system of points
    #  @param z Sequence of real numbers that represents coordinates
    #  @param m Sequence of real numbers that represents mass
    #  @return The overall center of mass of a system of points
    def __cm__(self, z, m):
        total = 0
        for i in range(len(m)):
            total += z[i] * m[i]
        return total / self.__sum__(m)

    ## @brief Gets the sum of the square of a coordinate pair added together
    #  mutiplied by their point mass
    #  @param x Sequence of real numbers that represents x coordinates
    #  @param y Sequence of real numbers that represents y coordinates
    #  @param m Sequence of real numbers that represents point masses
    #  @return The total value of the square of each coordinate pair added together
    #  mutiplied by their point mass
    def __mmom__(self, x, y, m):
        total = 0
        for i in range(len(m)):
            total += m[i] * (x[i]**2 + y[i]**2)
        return total
