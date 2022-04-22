## @file Plot.py
#  @author Mathew Petronilho
#  @brief Plotting functions
#  @date February 7, 2021

import matplotlib.pyplot as plt


## @brief Plots a three graphs from the given parameters
#  @details Plots the graph of x versus t, y versus t and y versus x
#  @param w A sequence of sequences with four real numbers
#  @param t A sequence of real numbers
#  @throws ValueError Throws an exception if w and t are not equal in length
def plot(w, t):
    if len(w) != len(t):
        raise ValueError

    x = [w[i][0] for i in range(len(w))]
    y = [w[i][1] for i in range(len(w))]

    fig, (ax1, ax2, ax3) = plt.subplots(3)
    fig.suptitle("Motion Simulation")
    ax1.plot(t, x)
    ax1.set(xlabel="t", ylabel="x(m)")
    ax2.plot(t, y)
    ax2.set(xlabel="t", ylabel="y(m)")
    ax3.plot(x, y)
    ax3.set(xlabel="x(m)", ylabel="y(m)")

    plt.show()
# Subplot idea from
# https://matplotlib.org/devdocs/gallery/subplots_axes_and_figures/subplots_demo.html
