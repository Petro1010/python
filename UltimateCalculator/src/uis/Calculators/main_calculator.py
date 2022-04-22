## @file main_calculator.py
#  @brief main calculator algorithms
#  @date April 5, 2022


## @brief Calculator is a class that implements the functionality of a basic calculator


class Calculator:

    ## @brief The constructor of the Calculator
    def __init__(self):
        self.lineEdit = ""  # actual calculation to be conducted
        self.currNum = ""   # number displayed to user
        self.mem = ""  # last remembered value

    ## @brief Retreives current displayed number
    def getCurrNum(self):
        return self.currNum

    ## @brief Stores the current number
    #  @details stores number for future use
    def storeMem(self):
        self.mem = self.currNum

    ## @brief Displays current stored number
    #  @details Checks if current stored number is empty and adds new number number to store and display
    def getMem(self):
        if (len(self.currNum) == 0):
            self.currNum = self.mem
            self.lineEdit += self.mem
    
    ## @brief Display value of input
    #  @details Adds the input v to the value of current number and displays it
    def valueInput(self, v):
        if len(self.currNum) < 20:
            self.lineEdit += v
            self.currNum += v
    
    ## @brief Empty the line and current number stored
    #  @details Clears the line value and the current number value to an empty string value and display new blank value
    def reset(self):
        self.lineEdit = ""
        self.currNum = ""
    
    ## @brief Conducts calculator addition operation
    #  @details Check if line input prior is not another operation and if it is not, display an empty string and adds an addition operation
    def addition(self):
        if len(self.lineEdit) > 0 and self.lineEdit[-1] not in ["+", "-", "/", "*"]: #make sure no two operations are done in a row
            self.lineEdit += "+"
            self.currNum = ""
    
    ## @brief Conducts calculator subtraction operation
    #  @details Check if line input prior is not another operation and if it is not, display an empty string and adds a subtraction operation
    def subtraction(self):
        if len(self.lineEdit) > 0 and self.lineEdit[-1] not in ["+", "-", "/", "*"]:
            self.lineEdit += "-"
            self.currNum = ""
    
    ## @brief Conducts calculator multiplication operation
    #  @details Check if line input prior is not another operation and if it is not, display an empty string and adds a multiplication operation
    def multiplication(self):
        if len(self.lineEdit) > 0 and self.lineEdit[-1] not in ["+", "-", "/", "*"]:
            self.lineEdit += "*"
            self.currNum = ""
    
    ## @brief Conducts calculator power operation
    #  @details Check if line input prior is not another operation and if it is not, display an empty string and adds a power operation
    def power(self):
        self.lineEdit += "**"
        self.currNum = ""
    
    ## @brief Conducts calculator division operation
    #  @details Check if line input prior is not another operation and if it is not, display an empty string and adds a division operation
    def division(self):
        if len(self.lineEdit) > 0 and self.lineEdit[-1] not in ["+", "-", "/", "*"]:
            self.lineEdit += "/"
            self.currNum = ""
    
    ## @brief Adds left bracket operation
    #  @details Clears the display and adds a left bracket to the operation
    def left_bracket(self):
        self.lineEdit += "("
        self.currNum = ""
    
    ## @brief Adds right bracket operation
    #  @details Clears the display and adds a right bracket to the operation
    def right_bracket(self):
        self.lineEdit += ")"
        self.currNum = ""
    
    ## @brief Evaluates operation 
    def evaluate(self):
        answer = eval(self.lineEdit)
        self.lineEdit = str(answer)
        #self.currNum = str(round(answer,4))
        self.currNum = format(float(answer), ".5")
    
    ## @brief Deletes entered input number by number
    def delete(self):
        if len(self.currNum) == 0:
                return

        if self.currNum[-1] == " ":  # Backspace two times if last text is blank/space
            self.currNum = self.currNum[:len(self.currNum) - 1]
            self.lineEdit = self.lineEdit[:len(self.lineEdit) - 1]

        self.currNum = self.currNum[:len(self.currNum) - 1]
        self.lineEdit = self.lineEdit[:len(self.lineEdit) - 1]
