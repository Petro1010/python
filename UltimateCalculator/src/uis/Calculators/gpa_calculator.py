## @file gpa_calculator.py
#  @brief gpa algorithms
#  @date March 17, 2022

## @brief Calculates the GPA of the user
#  @param gradeList A list with floats that carries the grades of each class multipled
#  by the weight of the class.
#  @return The average GPA of the student
#  @throws ZeroDivisionError Throws an exception if weightTotal is zero
def gpaCalculate(gradeList, weightTotal):
	if(weightTotal == 0):
		raise ZeroDivisionError

	gpatotal = 0.0
	for i in gradeList:
		gpatotal = gpatotal + i
	return format(gpatotal/weightTotal, ".4")