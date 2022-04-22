## @file floating_point_ui.py
#  @brief Provides a class to display the Floating Point window
#  @date March 18, 2022

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from uis.Calculators.binary_calculator import toFloatingPoint, toDecimal

## @brief FloatingPointWindow is a class that implements the GUI components for the Floating Point operation

class FloatingPointWindow(QMainWindow):

    ## @brief The constructor of the Floating Point window
    #  @details Creates a pop up window that displays and sets up the buttons and input fields that are
    #  necessary to obtain input from the user and calculate the appropriate answer.
    #  Also sets up the window according to the created style sheet.
    #  @param path The current path on which the file is found. Default value is an empty path.
    def __init__(self, path=""):
        super(FloatingPointWindow, self).__init__()

        self.path = f"{path}Ui_Base/floatingPoint.ui"
        loadUi(self.path, self)

        self.setFixedSize(679, 453)

        self.go_btn.clicked.connect(self.floating_point)
        self.exit_btn.clicked.connect(self.close)
        self.clr_btn.clicked.connect(self.clearFields)

    ## @brief Displays the conversion of a decimal number to IEEE 754 floating point representation and vice versa
    #  @details Takes in decimal number or floating point number from the user through input
    #  fields, and shows the user the result on the window
    def floating_point(self):
        choice = self.comboBox.currentText()
        try:
            if choice == "Decimal to Double Precision IEEE-754":
                n = float(self.line_2.text())
                val = toFloatingPoint(n)
                self.line_3.setText(val)
        except:
            self.clearFields()
            self.line_3.setText("Invalid Input!")
        
        try:
            if choice == "Double Precision IEEE-754 to Decimal":
                n = self.line_2.text()
                val = toDecimal(n)
                self.line_3.setText(val)
        except:
            self.clearFields()
            self.line_3.setText("Invalid Input! Please enter a binary number of length \'64\'")
        

    ## @brief Closes window and clears inputs upon close
    def closeEvent(self, event):
        self.clearFields()
        event.accept()

    ## @brief Clears all input and output fields
    def clearFields(self):
        self.line_2.setText("")
        self.line_3.setText("")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = FloatingPointWindow()
    window.show()
    sys.exit(app.exec_())