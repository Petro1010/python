## @file y_int_ui.py
#  @brief Provides a class to display the Y-intercept window
#  @date March 30, 2022

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from uis.Calculators.algebra_calculator import yIntercept

## @brief Slope2Window is a class that implements the GUI components
#  for the Y-intercept operation


class YintWindow(QMainWindow):

    ## @brief The constructor of the Y-intercept window
    #  @details Creates a pop up window that displays and
    #  sets up the buttons and input fields that are necessary
    #  to obtain input from the user and calculate the appropriate answer.
    #  Also sets up the window according to the created style sheet.
    #  @param path The current path on which the file is found.
    #  Default value is an empty path.
    def __init__(self, path=""):
        super(YintWindow, self).__init__()

        self.path = f"{path}Ui_Base/y_int.ui"
        loadUi(self.path, self)

        self.setFixedSize(391, 547)

        self.go_btn.clicked.connect(self.yInt)
        self.exit_btn.clicked.connect(self.close)
        self.clr_btn.clicked.connect(self.clearFields)

    ## @brief Displays the y-intercept of the given slope and coordinate
    #  @details Takes the inputs of a slope and a coordinate
    #  from the user through input
    #  fields, and shows the user the result on the window
    def yInt(self):
        try:
            m = float(self.line_1.text())
            x = float(self.line_2.text())
            y = float(self.line_3.text())
            b = yIntercept(m, x, y)
            self.line_4.setText(b)
        except ValueError:
            self.clearFields()
            self.line_4.setText("Invalid Input!")

    ## @brief Resets inputs and closes window
    def closeEvent(self, event):
        self.clearFields()
        event.accept()

    ## @brief Clears all input and output fields
    def clearFields(self):
        self.line_1.setText("")
        self.line_2.setText("")
        self.line_3.setText("")
        self.line_4.setText("")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = YintWindow()
    window.show()
    sys.exit(app.exec_())
