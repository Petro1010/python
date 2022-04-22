## @file health_calculator.py
#  @brief Health algorithms
#  @date March 31, 2022

## @brief Calculates the body mass index of a person
#  @param weight A real number that represents the weight of the user in pounds
#  @param height A real number that represents the height of the user in inches
#  @return A tuple of bmi coefficient and a string with its meaning
#  @throws ValueError Throws an exception if height or weight is not valid
#  @throws ZeroDivisionError Throws an exception if height is 0
def bodyMassIndex(weight, height):
    if not(height):
        raise ZeroDivisionError

    if height < 0 or weight <= 0:
        raise ValueError

    bmi = (703*weight)/(height**2)
    # Meaning of BMI according to WHO:
    message = ""
    if bmi < 16:
        message = "Indicates Severe Thinness"
    elif bmi < 17:
        message = "Indicates Moderate Thinness"
    elif bmi < 18.5:
        message = "Indicates Mild Thinness"
    elif bmi < 25:
        message = "Indicates Normal Weight"
    elif bmi < 30:
        message = "Indicates Overweight"
    elif bmi < 35:
        message = "Indicates Mild Obesity"
    elif bmi < 40:
        message = "Indicates Moderate Obesity"
    else:
        message = "Indicates Severe Obesity"

    return (format(bmi, ".13"), message)


## @brief Calculates the body fat percentage of a person
#  @param gender A string that represents the gender of the person
#  @param height A real number that represents the height of the user in inches
#  @param weight A real number that represents the weight of the user in pounds
#  @param age A real number that represents how old the person is
#  @return A tuple of body fat percentage and a string with its meaning
#  @throws ValueError Throws an exception if a measurement is not valid
#  @throws ZeroDivisionError Throws an exception if height is 0
def bodyFat(weight, height, gender, age):
    if not(height):
        raise ZeroDivisionError

    if height < 0 or weight <= 0 or age <= 0:
        raise ValueError

    if gender == "Female":
        bf = 1.2*((703*weight)/(height**2)) + 0.23*age - 5.4
    else:
        bf = 1.2*((703*weight)/(height**2)) + 0.23*age - 16.2

    # Based on American Council Excercise Body Fat Categorization
    message = ""
    if (gender == "Female" and bf < 10) or (gender == "Male" and bf < 2):
        message = "Indicates Less than Essential Fat"
    elif (gender == "Female" and bf < 13) or (gender == "Male" and bf < 5):
        message = "Indicates Essential Fat"
    elif (gender == "Female" and bf < 20) or (gender == "Male" and bf < 13):
        message = "Indicates you are an Athlete"
    elif (gender == "Female" and bf < 24) or (gender == "Male" and bf < 17):
        message = "Indicates you are Fit"
    elif (gender == "Female" and bf < 31) or (gender == "Male" and bf < 24):
        message = "Indicates Average Fat"
    else:
        message = "Indicates Obesity"

    return (format(bf, ".13"), message)
