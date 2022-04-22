## @file perimeter_ui.py
#  @brief Provides a class to display the Perimeter window
#  @date March 18, 2022

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from uis.Calculators.geometry_calculator import getPerimeter

## @brief PerimeterWindow is a class that implements the GUI components for the Perimeter operation

class PerimeterWindow(QMainWindow):

    ## @brief The constructor of the Perimeter window
    #  @details Creates a pop up window that displays and sets up the buttons and input fields that are
    #  necessary to obtain input from the user and calculate the appropriate answer.
    #  Also sets up the window according to the created style sheet.
    #  @param path The current path on which the file is found. Default value is an empty path.
    def __init__(self, path=""):
        super(PerimeterWindow, self).__init__()

        self.path = f"{path}Ui_Base/perimeter.ui"
        loadUi(self.path, self)

        self.setFixedSize(401, 651)  
        self.line_2.setReadOnly(False)
        self.line_3.setReadOnly(True)
        self.line_4.setReadOnly(True)
        self.line_5.setReadOnly(True)
        self.line_3.setText("N/A")
        self.line_4.setText("N/A")
        self.line_5.setText("N/A")

        self.go_btn.clicked.connect(self.perimeter)
        self.exit_btn.clicked.connect(self.close)
        self.clr_btn.clicked.connect(self.clearFields)
        self.comboBox.currentTextChanged.connect(self.setFields)

    ## @brief Displays the perimeter of selected shape given appropriate side lengths/radius
    #  @details Takes in up to 3 side lengths and a radius as input from the user through input
    #  fields, and shows the user the result on the window
    def perimeter(self):
        try:
            shape = self.comboBox.currentText()
            if shape == "Square":
                side_a = float(self.line_2.text())
                val = getPerimeter(0, side_a, None, None, None)
            elif shape == "Rectangle":
                side_a = float(self.line_2.text())
                side_b = float(self.line_3.text())
                val = getPerimeter(1, side_a, side_b, None, None)
            elif shape == "Triangle":
                side_a = float(self.line_2.text())
                side_b = float(self.line_3.text())
                side_c = float(self.line_4.text())
                val = getPerimeter(2, side_a, side_b, side_c, None)
            elif shape == "Circle":
                radius = float(self.line_5.text())
                val = getPerimeter(3, None, None, None, radius)
            self.line_6.setText(str(val))
        except:
            self.clearFields()
            self.line_6.setText("Invalid Input!")

    ## @brief Changes and displays in text boxes corresponding to chosen shape
    def setFields(self):
        shape = self.comboBox.currentText()
        if shape == "Square":
            self.clearFields()
            self.line_2.setReadOnly(False)
            self.line_3.setReadOnly(True)
            self.line_4.setReadOnly(True)
            self.line_5.setReadOnly(True)
            self.line_3.setText("N/A")
            self.line_4.setText("N/A")
            self.line_5.setText("N/A")
        elif shape == "Rectangle":
            self.clearFields()
            self.line_2.setReadOnly(False)
            self.line_3.setReadOnly(False)
            self.line_4.setReadOnly(True)
            self.line_5.setReadOnly(True)
            self.line_4.setText("N/A")
            self.line_5.setText("N/A")
        elif shape == "Triangle":
            self.clearFields()
            self.line_2.setReadOnly(False)
            self.line_3.setReadOnly(False)
            self.line_4.setReadOnly(False)
            self.line_5.setReadOnly(True)
            self.line_5.setText("N/A")
        elif shape == "Circle":
            self.clearFields()
            self.line_2.setReadOnly(True)
            self.line_3.setReadOnly(True)
            self.line_4.setReadOnly(True)
            self.line_5.setReadOnly(False)
            self.line_2.setText("N/A")
            self.line_3.setText("N/A")
            self.line_4.setText("N/A")

    ## @brief Closes window and clears inputs upon close
    def closeEvent(self, event):
        self.clearFields()
        event.accept()

    ## @brief Clears all input and output fields
    def clearFields(self):
        shape = self.comboBox.currentText()
        if shape == "Square":
            self.line_2.setText("")
        elif shape == "Rectangle":
            self.line_2.setText("")
            self.line_3.setText("")
        elif shape == "Triangle":
            self.line_2.setText("")
            self.line_3.setText("")
            self.line_4.setText("")
        elif shape == "Circle":
            self.line_5.setText("")
        self.line_6.setText("")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = PerimeterWindow()
    window.show()
    sys.exit(app.exec_())