## @file binary_arithmetic_ui.py
#  @brief Provides a class to display the Binary Arithmetic window
#  @date March 18, 2022

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from uis.Calculators.binary_calculator import binAdd, binSub, binMult, binDiv, binPow

## @brief BinArithmeticWindow is a class that implements the GUI components for the Binary Arithmetic operations

class BinArithmeticWindow(QMainWindow):

    ## @brief The constructor of the Binary Arithmetic window
    #  @details Creates a pop up window that displays and sets up the buttons and input fields that are
    #  necessary to obtain input from the user and calculate the appropriate answer.
    #  Also sets up the window according to the created style sheet.
    #  @param path The current path on which the file is found. Default value is an empty path.
    def __init__(self, path=""):
        super(BinArithmeticWindow, self).__init__()

        self.path = f"{path}Ui_Base/binaryArithmetic.ui"
        loadUi(self.path, self)

        self.setFixedSize(549, 514)

        self.go_btn.clicked.connect(self.binArithmetic)
        self.exit_btn.clicked.connect(self.close)
        self.clr_btn.clicked.connect(self.clearFields)

    ## @brief Displays the arithmetic output of two binary numbers using various operators
    #  @details Takes in two binary numbers and the operator from the user through input
    #  fields, and shows the user the result on the window
    def binArithmetic(self):
        operator = self.comboBox.currentText()
        try:
            if operator == "+":
                n = int(self.line_1.text(), 2)
                m = int(self.line_3.text(), 2)
                val = binAdd(n, m)
            elif operator == "-":
                n = int(self.line_1.text(), 2)
                m = int(self.line_3.text(), 2)
                val = binSub(n, m)
            elif operator == "*":
                n = int(self.line_1.text(), 2)
                m = int(self.line_3.text(), 2)
                val = binMult(n, m)
            elif operator == "/":
                n = int(self.line_1.text(), 2)
                m = int(self.line_3.text(), 2)
                val = binDiv(n, m)
            elif operator == "^":
                n = int(self.line_1.text(), 2)
                m = int(self.line_3.text(), 2)
                val = binPow(n, m)
            self.line_4.setText(val)
        except ValueError:
            self.clearFields()
            self.line_4.setText("Invalid Input!")
        except ZeroDivisionError:
            self.clearFields()
            self.line_4.setText("Division by Zero!")

    ## @brief Closes window and clears inputs upon close
    def closeEvent(self, event):
        self.clearFields()
        event.accept()

    ## @brief Clears all input and output fields
    def clearFields(self):
        self.line_1.setText("")
        self.line_3.setText("")
        self.line_4.setText("")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = BinArithmeticWindow()
    window.show()
    sys.exit(app.exec_())