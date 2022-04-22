## @file Shape.py
#  @author Mathew Petronilho
#  @brief An interface for shapes
#  @date February 2, 2021


from abc import ABC, abstractmethod

## @brief Shape contains a generic structure for different shapes


class Shape(ABC):

    @abstractmethod
    ## @brief a generic method to get the x coordinate of the center of mass of the shape
    #  @return a real number that represents the x coordinate of the center of mass
    def cm_x(self):
        pass

    @abstractmethod
    ## @brief a generic method to get the y coordinate of the center of mass of the shape
    #  @return a real number that represents the y coordinate of the center of mass
    def cm_y(self):
        pass

    @abstractmethod
    ## @brief a generic method to get the mass of the shape
    #  @return a real number that represents the mass of the shape
    def mass(self):
        pass

    @abstractmethod
    ## @brief a generic method to get the moment of inertia of the shape
    #  @return a real number that represents the moment of inertia of the shape
    def m_inert(self):
        pass
