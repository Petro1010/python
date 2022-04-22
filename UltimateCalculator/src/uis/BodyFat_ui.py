## @file BodyFat_ui.py
#  @brief Provides a class to display the Body Fat window
#  @date March 30, 2022

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from uis.Calculators.health_calculator import bodyFat

## @brief BFWindow is a class that implements the GUI components
#  for the Body Fat operation


class BFWindow(QMainWindow):

    ## @brief The constructor of the Body Fat window
    #  @details Creates a pop up window that displays and sets up the buttons
    #  and input fields that are necessary to obtain input from the user and
    #  calculate the appropriate answer. Also sets up the window according
    #  to the created style sheet.
    #  @param path The current path on which the file is found.
    #  Default value is an empty path.
    def __init__(self, path=""):
        super(BFWindow, self).__init__()

        self.path = f"{path}Ui_Base/BF.ui"
        loadUi(self.path, self)

        self.setFixedSize(461, 669)

        self.go_btn.clicked.connect(self.bf)
        self.exit_btn.clicked.connect(self.close)
        self.clr_btn.clicked.connect(self.clearFields)

    ## @brief Displays the Body Fat rating and its meaning
    #  based on the metrics the user provides
    #  @details Takes in age, gender, height, and weight from the user
    #  through input fields, and shows the user the result on the window
    def bf(self):
        try:
            gender = self.genderComboBox.currentText()
            height_feet = float(self.feet.text())
            height_inches = float(self.inches.text())
            height = 12*height_feet + height_inches
            weight = float(self.weight.text())
            age = float(self.age.text())

            bf, message = bodyFat(weight, height, gender, age)
            self.bf_result.setText(str(bf))
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
        self.age.setText("")
        self.bf_result.setText("")
        self.meaning.setText("")
        self.genderComboBox.setCurrentText("")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = BFWindow()
    window.show()
    sys.exit(app.exec_())
