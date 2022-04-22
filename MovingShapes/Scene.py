## @file Scene.py
#  @author Mathew Petronilho
#  @brief Provides the environment for which your shape is travelling in
#  @date February 7, 2021

from scipy import integrate

## @brief Scene is a class that provides the simulation of the movement of a shape object
#  @details This movement is determined by the type of shape, forces and velocity


class Scene():

    ## @brief Scene constructor
    #  @details Creates a scene for which a shape has unbalanced forces and velocity. We
    #  assume all parameters will be of the correct type.
    #  @param s An object of the type Shape
    #  @param Fx The unbalanced force function in the x direction
    #  @param Fy The unbalanced force function in the y direction
    #  @param vx The initial velocity of the shape in the x direction
    #  @param vy The initial velocity of the shape in the y direction
    def __init__(self, s, Fx, Fy, vx, vy):
        self.s = s
        self.Fx = Fx
        self.Fy = Fy
        self.vx = vx
        self.vy = vy

    ## @brief Gets the shape in the scene
    #  @return An object of type Shape
    def get_shape(self):
        return self.s

    ## @brief Gets the unbalanced force functions of the shape
    #  @return A tuple of the unbalanced force functions
    def get_unbal_forces(self):
        return self.Fx, self.Fy

    ## @brief Gets the initial velocity of the shape
    #  @return A tuple of the initial velocities in the x and y directions
    def get_init_velo(self):
        return self.vx, self.vy

    ## @brief Changes the type of shape that is in the scene
    #  @details Changes the shape value of the constructor to a different shape
    #  @param s A shape object
    #  @return Does not return anything
    def set_shape(self, s):
        self.s = s

    ## @brief Changes the unbalanced force functions on the shape in the scene
    #  @details Changes the function values of the constructor to different functions
    #  @param Fx A function representing the unbalanced force in the x direction
    #  @param Fy A function representing the unbalanced force in the y direction
    #  @return Does not return anything
    def set_unbal_forces(self, Fx, Fy):
        self.Fx = Fx
        self.Fy = Fy

    ## @brief Changes the inital velocity of the shape in the scene
    #  @details Changes the initial velocity values of the constructor to different values
    #  @param vx A real number representing new velocity in the x direction
    #  @param vy A real number representing new velocity in the y direction
    #  @return Does not return anything
    def set_init_velo(self, vx, vy):
        self.vx = vx
        self.vy = vy

    ## @brief Creates a simulation of the movement of the shape in the given scene
    #  @param t_final A real number representing the total time the sim runs for
    #  @param nsteps A natural number representing the amount of steps in the sim
    #  @return A tuple that contains a sequence of times and a sequence of four sequences that
    #  contain the position of the shape in the x and y axis and its velocity
    def sim(self, t_final, nsteps):
        t = [(i * t_final) / (nsteps - 1) for i in range(0, nsteps)]
        lst = [self.s.cm_x(), self.s.cm_y(), self.vx, self.vy]
        return t, integrate.odeint(self.__ode__, lst, t)

    ## @brief Ordinary differential equation formulator
    #  @param w A sequence of four numbers that represents the shape position and velocity
    #  @param t A number representing time
    #  @return A sequence of real numbers
    def __ode__(self, w, t):
        return [w[2], w[3], self.Fx(t) / self.s.mass(), self.Fy(t) / self.s.mass()]
