## @file algebra_calculator.py
#  @brief Alegbraic algorithms
#  @date March 17, 2022

## @brief Calculates slope of a line given 2 points
#  @param x1 A real number that represents the X-coordinate of the first point
#  @param y1 A real number that represents the Y-coordinate of the first point
#  @param x2 A real number that represents the X-coordinate of the second point
#  @param y2 A real number that represents the Y-coordinate of the second point
#  @return The slope of the line
#  @throws ZeroDivisionError Throws an exception if x2 and x1 are equal
def slopeOfLine(x1, y1, x2, y2):
    if not(x2 - x1):
        raise ZeroDivisionError

    return format((y2 - y1) / (x2 - x1), ".13")


## @brief Calculates y-intercept of a line given a point and the slope
#  @param m A real number that represents the slope of the line
#  @param x A real number that represents the X-coordinate of the point
#  @param y A real number that represents the Y-coordinate of the point
#  @return The y-intercept of the line
def yIntercept(m, x, y):
    return format(y - (m*x), ".13")


## @brief Calculates pythagorean theorem of a right triangle
#  given two sides and the side to solve for
#  @param solve A string that represents the missing side
#  @param a A real number that represents a side the is not the hypotenuse
#  @param b A real number that represents a side the is not the hypotenuse
#  @param c A real number that represents the hypotenuse
#  @return The length of the missing side
#  @throws ValueError Throws an exception if hypotenuse is not the longest side
#  or sides are not postive
def pyTheorem(solve, a, b, c):
    ans = None
    if solve == "C":
        if a <= 0 or b <= 0:
            raise ValueError

        ans = (a**2 + b**2)**(1/2)
    elif solve == "B":
        if a <= 0 or c <= 0 or a > c:
            raise ValueError

        ans = (c**2 - a**2)**(1/2)

    else:
        if b <= 0 or c <= 0 or b > c:
            raise ValueError

        ans = (c**2 - b**2)**(1/2)

    return format(ans, ".13")
