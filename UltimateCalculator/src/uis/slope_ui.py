## @file slope_ui.py
#  @brief Provides a class to display the Slope window
#  @date March 30, 2022

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from uis.Calculators.algebra_calculator import slopeOfLine

## @brief Slope1Window is a class that implements the GUI components
#  for the Slope operation


class SlopeWindow(QMainWindow):

    ## @brief The constructor of the Slope window
    #  @details Creates a pop up window that displays and sets up the buttons
    #  and input fields that are necessary to obtain input from the user and
    #  calculate the appropriate answer. Also sets up the window according to
    #  the created style sheet.
    #  @param path The current path on which the file is found.
    #  Default value is an empty path.
    def __init__(self, path=""):
        super(SlopeWindow, self).__init__()

        self.path = f"{path}Ui_Base/slope.ui"
        loadUi(self.path, self)

        self.setFixedSize(403, 592)

        self.go_btn.clicked.connect(self.slope)
        self.exit_btn.clicked.connect(self.close)
        self.clr_btn.clicked.connect(self.clearFields)

    ## @brief Displays the slope of a line given two coordinates
    #  @details Takes in two coordinates as input from the user through input
    #  fields, and shows the user the result on the window
    def slope(self):
        try:
            y2 = float(self.line_1.text())
            y1 = float(self.line_2.text())
            x2 = float(self.line_3.text())
            x1 = float(self.line_4.text())

            slope = slopeOfLine(x1, y1, x2, y2)
            self.line_5.setText(slope)
        except ValueError:
            self.clearFields()
            self.line_5.setText("Invalid Input!")

        except ZeroDivisionError:
            self.clearFields()
            self.line_5.setText("Division By Zero!")

    ## @brief Closes window and clears inputs upon close
    def closeEvent(self, event):
        self.clearFields()
        event.accept()

    ## @brief Clears all input and output fields
    def clearFields(self):
        self.line_1.setText("")
        self.line_2.setText("")
        self.line_3.setText("")
        self.line_4.setText("")
        self.line_5.setText("")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = SlopeWindow()
    window.show()
    sys.exit(app.exec_())
