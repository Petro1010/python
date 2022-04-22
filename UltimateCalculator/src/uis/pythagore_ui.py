## @file pythagore_ui.py
#  @brief Provides a class to display the Pythagorean Theorem window
#  @date March 30, 2022

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from uis.Calculators.algebra_calculator import pyTheorem

## @brief PythaWindow is a class that implements the GUI components
#  for the Pythagorean Theorem operation


class PythaWindow(QMainWindow):

    ## @brief The constructor of the Pythagorean Theorem window
    #  @details Creates a pop up window that displays and sets up the
    #  buttons and input fields that are necessary to obtain input from
    #  the user and calculate the appropriate answer. Also sets up the
    #  window according to the created style sheet.
    #  @param path The current path on which the file is found.
    #  Default value is an empty path.
    def __init__(self, path=""):
        super(PythaWindow, self).__init__()

        self.path = f"{path}Ui_Base/pythagore.ui"
        loadUi(self.path, self)

        self.setFixedSize(470, 503)

        self.go_btn.clicked.connect(self.pytha)
        self.exit_btn.clicked.connect(self.close)
        self.clr_btn.clicked.connect(self.clearFields)

    ## @brief Displays the length of the missing side of a right angle triangle
    #  @details Takes the inputs of two sides from the user through input
    #  fields, and shows the user the length of the missing side on the window
    def pytha(self):
        try:
            side = self.comboBox.currentText()
            if side == "A":
                b = float(self.line_2.text())
                c = float(self.line_3.text())
                a = pyTheorem("A", None, b, c)
                self.line_1.setText(a)
            elif side == "B":
                a = float(self.line_1.text())
                c = float(self.line_3.text())
                b = pyTheorem("B", a, None, c)
                self.line_2.setText(b)
            elif side == "C":
                a = float(self.line_1.text())
                b = float(self.line_2.text())
                c = pyTheorem("C", a, b, None)
                self.line_3.setText(c)
        except ValueError:
            self.line_1.setText("Invalid Input!")
            self.line_2.setText("Invalid Input!")
            self.line_3.setText("Invalid Input!")

    ## @brief Resets fields upon close of window
    def closeEvent(self, event):
        self.clearFields()
        event.accept()

    ## @brief Clears all input and output fields
    def clearFields(self):
        self.line_1.setText("")
        self.line_2.setText("")
        self.line_3.setText("")
        self.comboBox.setCurrentText("")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = PythaWindow()
    window.show()
    sys.exit(app.exec_())
