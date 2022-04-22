## @file BMI_ui.py
#  @brief Provides a class to display the BMI window
#  @date March 30, 2022

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from uis.Calculators.health_calculator import bodyMassIndex

## @brief BMIWindow is a class that implements the GUI components
#  for the BMI operation


class BMIWindow(QMainWindow):

    ## @brief The constructor of the BMI window
    #  @details Creates a pop up window that displays and sets up the buttons
    #  and input fields that are necessary to obtain input from the user
    #  and calculate the appropriate answer.
    #  Also sets up the window according to the created style sheet.
    #  @param path The current path on which the file is found.
    #  Default value is an empty path.
    def __init__(self, path=""):
        super(BMIWindow, self).__init__()

        self.path = f"{path}Ui_Base/BMI.ui"
        loadUi(self.path, self)

        self.setFixedSize(402, 581)

        self.go_btn.clicked.connect(self.bmi)
        self.exit_btn.clicked.connect(self.close)
        self.clr_btn.clicked.connect(self.clearFields)

    ## @brief Displays the BMI and its meaning based on the metrics
    #  the user provides
    #  @details Takes in height and weight from the user through input
    #  fields, and shows the user the result on the window
    def bmi(self):
        try:
            weight = float(self.weight.text())
            height_feet = float(self.feet.text())
            height_inches = float(self.inches.text())
            height = 12*height_feet + height_inches

            bmi, message = bodyMassIndex(weight, height)
            self.bmi_result.setText(str(bmi))
            self.meaning.setText(message)
        except ZeroDivisionError:
            self.clearFields()
            self.meaning.setText("Division By Zero!")

        except ValueError:
            self.clearFields()
            self.meaning.setText("Invalid Input!")

    ## @brief Resets fields and closes window
    def closeEvent(self, event):
        self.clearFields()
        event.accept()

    ## @brief Clears all input and output fields
    def clearFields(self):
        self.weight.setText("")
        self.feet.setText("")
        self.inches.setText("")
        self.bmi_result.setText("")
        self.meaning.setText("")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = BMIWindow()
    window.show()
    sys.exit(app.exec_())
