## @file bitwise_ui.py
#  @brief Provides a class to display the Bitwise Operation window
#  @date March 18, 2022

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from uis.Calculators.binary_calculator import bitwiseAND, bitwiseOR, bitwiseNOT, bitwiseXOR, rshift, lshift

## @brief BitwiseWindow is a class that implements the GUI components for the Bitwise operations

class BitwiseWindow(QMainWindow):

    ## @brief The constructor of the Bitwise window
    #  @details Creates a pop up window that displays and sets up the buttons and input fields that are
    #  necessary to obtain input from the user and calculate the appropriate answer.
    #  Also sets up the window according to the created style sheet.
    #  @param path The current path on which the file is found. Default value is an empty path.
    def __init__(self, path=""):
        super(BitwiseWindow, self).__init__()

        self.path = f"{path}Ui_Base/bitwise.ui"
        loadUi(self.path, self)

        self.setFixedSize(542, 572)
        self.clearFields()
        self.line_3.setReadOnly(False)
        self.line_4.setReadOnly(True)
        self.line_5.setReadOnly(True)
        self.line_4.setText("N/A")
        self.line_5.setText("N/A")

        self.go_btn.clicked.connect(self.bitwise)
        self.exit_btn.clicked.connect(self.close)
        self.clr_btn.clicked.connect(self.clearFields)
        self.comboBox.currentTextChanged.connect(self.setFields)

    ## @brief Displays the output of bitwise operations on one or two binary numbers
    #  @details Takes in one or two binary numbers and the operator from the user through input
    #  fields, and shows the user the result on the window
    def bitwise(self):
        operator = self.comboBox.currentText()
        try:
            if operator == "AND":
                n = int(self.line_1.text(), 2)
                m = int(self.line_3.text(), 2)
                val = bitwiseAND(n, m)
            elif operator == "OR":
                n = int(self.line_1.text(), 2)
                m = int(self.line_3.text(), 2)
                val = bitwiseOR(n, m)
            elif operator == "NOT":
                n = int(self.line_1.text(), 2)
                val = bitwiseNOT(n)
            elif operator == "XOR":
                n = int(self.line_1.text(), 2)
                m = int(self.line_3.text(), 2)
                val = bitwiseXOR(n, m)
            elif operator == "SHIFT RIGHT":
                n = int(self.line_1.text(), 2)
                shiftBy = int(self.line_4.text())
                length = int(self.line_5.text())
                val = rshift(n, shiftBy, length)
            elif operator == "SHIFT LEFT":
                n = int(self.line_1.text(), 2)
                shiftBy = int(self.line_4.text())
                length = int(self.line_5.text())
                val = lshift(n, shiftBy, length)
            self.line_6.setText(val)
        except:
           self.line_6.setText("Invalid Input!")
    
    ## @brief Changes and displays in text boxes corresponding to chosen operator
    def setFields(self):
        operator = self.comboBox.currentText()
        if operator == "AND":
            self.clearFields()
            self.line_3.setReadOnly(False)
            self.line_4.setReadOnly(True)
            self.line_5.setReadOnly(True)
            self.line_4.setText("N/A")
            self.line_5.setText("N/A")
        elif operator == "OR":
            self.clearFields()
            self.line_3.setReadOnly(False)
            self.line_4.setReadOnly(True)
            self.line_5.setReadOnly(True)
            self.line_4.setText("N/A")
            self.line_5.setText("N/A")
        elif operator == "NOT":
            self.clearFields()
            self.line_3.setReadOnly(True)
            self.line_4.setReadOnly(True)
            self.line_5.setReadOnly(True)
            self.line_3.setText("N/A")
            self.line_4.setText("N/A")
            self.line_5.setText("N/A")
        elif operator == "XOR":
            self.clearFields()
            self.line_3.setReadOnly(False)
            self.line_4.setReadOnly(True)
            self.line_5.setReadOnly(True)
            self.line_4.setText("N/A")
            self.line_5.setText("N/A")
        elif operator == "SHIFT RIGHT":
            self.clearFields()
            self.line_3.setReadOnly(True)
            self.line_4.setReadOnly(False)
            self.line_5.setReadOnly(False)
            self.line_3.setText("N/A")
        elif operator == "SHIFT LEFT":
            self.clearFields()
            self.line_3.setReadOnly(True)
            self.line_4.setReadOnly(False)
            self.line_5.setReadOnly(False)
            self.line_3.setText("N/A")

    ## @brief Closes window and clears inputs upon close
    def closeEvent(self, event):
        self.clearFields()
        event.accept()

    ## @brief Clears all input and output fields
    def clearFields(self):
        operator = self.comboBox.currentText()
        self.line_1.setText("")
        if operator == "AND":
            self.line_3.setText("")
            self.line_6.setText("")
        elif operator == "OR":
            self.line_3.setText("")
            self.line_6.setText("")
        elif operator == "NOT":
            self.line_6.setText("")
        elif operator == "XOR":
            self.line_3.setText("")
            self.line_6.setText("")
        elif operator == "SHIFT RIGHT":
            self.line_4.setText("")
            self.line_5.setText("")
            self.line_6.setText("")
        elif operator == "SHIFT LEFT":
            self.line_4.setText("")
            self.line_5.setText("")
            self.line_6.setText("")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = BitwiseWindow()
    window.show()
    sys.exit(app.exec_())