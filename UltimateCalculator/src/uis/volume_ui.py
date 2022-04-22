## @file volume_ui.py
#  @brief Provides a class to display the Volume window
#  @date March 18, 2022

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from uis.Calculators.geometry_calculator import getVolume

## @brief VolumeWindow is a class that implements the GUI components for the Volume operation

class VolumeWindow(QMainWindow):

    ## @brief The constructor of the Volume window
    #  @details Creates a pop up window that displays and sets up the buttons and input fields that are
    #  necessary to obtain input from the user and calculate the appropriate answer.
    #  Also sets up the window according to the created style sheet.
    #  @param path The current path on which the file is found. Default value is an empty path.
    def __init__(self, path=""):
        super(VolumeWindow, self).__init__()

        self.path = f"{path}Ui_Base/volume.ui"
        loadUi(self.path, self)
        
        self.setFixedSize(401, 651)
        self.line_2.setReadOnly(False)
        self.line_3.setReadOnly(True)
        self.line_4.setReadOnly(True)
        self.line_5.setReadOnly(True)
        self.line_3.setText("N/A")
        self.line_4.setText("N/A")
        self.line_5.setText("N/A")

        self.go_btn.clicked.connect(self.volume)
        self.exit_btn.clicked.connect(self.close)
        self.clr_btn.clicked.connect(self.clearFields)
        self.comboBox.currentTextChanged.connect(self.setFields)

    ## @brief Displays the volume of selected 3D shape given appropriate dimensions
    #  @details Takes in up to 3 dimensions and/or radius as input from the user through input
    #  fields, and shows the user the result on the window
    def volume(self):
        try:
            shape = self.comboBox.currentText()
            if shape == "Cube":
                l = float(self.line_2.text())
                val = getVolume(0, l, None, None, None)
            elif shape == "Rectangular Prism":
                l = float(self.line_2.text())
                w = float(self.line_3.text())
                h = float(self.line_4.text())
                val = getVolume(1, l, w, h, None)
            elif shape == "Cylinder":
                h = float(self.line_4.text())
                radius = float(self.line_5.text())
                val = getVolume(2, None, None, h, radius)
            elif shape == "Sphere":
                radius = float(self.line_5.text())
                val = getVolume(3, None, None, None, radius)
            self.line_6.setText(str(val))
        except:
            self.clearFields()
            self.line_6.setText("Invalid Input!")

    ## @brief Changes and displays in text boxes corresponding to chosen shape
    def setFields(self):
        shape = self.comboBox.currentText()
        if shape == "Cube":
            self.clearFields()
            self.line_2.setReadOnly(False)
            self.line_3.setReadOnly(True)
            self.line_4.setReadOnly(True)
            self.line_5.setReadOnly(True)
            self.line_3.setText("N/A")
            self.line_4.setText("N/A")
            self.line_5.setText("N/A")
        elif shape == "Rectangular Prism":
            self.clearFields()
            self.line_2.setReadOnly(False)
            self.line_3.setReadOnly(False)
            self.line_4.setReadOnly(False)
            self.line_5.setReadOnly(True)
            self.line_5.setText("N/A")
        elif shape == "Cylinder":
            self.clearFields()
            self.line_2.setReadOnly(True)
            self.line_3.setReadOnly(True)
            self.line_4.setReadOnly(False)
            self.line_5.setReadOnly(False)
            self.line_2.setText("N/A")
            self.line_3.setText("N/A")
        elif shape == "Sphere":
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
    window = VolumeWindow()
    window.show()
    sys.exit(app.exec_())