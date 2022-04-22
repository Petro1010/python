## @file gpa_ui.py
#  @brief Provides a class to display the GPA window
#  @date March 17, 2022

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from uis.Calculators.gpa_calculator import gpaCalculate

## @brief GPAWindow is a class that implements the GUI components for the GPA operation menu

class GPAWindow(QMainWindow):

    ## @brief The constructor of the GPA window
    #  @details Creates a pop up window that displays and sets up the buttons that are
    #  necessary to navigate from the GPA window to other parts of the application.
    #  Also sets up the GPA window according to the created style sheet.
    #  @param path The current path on which the file is found. Default value is an empty path.

    gradeList = []
    index = 0
    totalWeight = 0
    
    def __init__(self, path=""):
        super(GPAWindow, self).__init__()

        self.path = f"{path}Ui_Base/gpa.ui"
        loadUi(self.path, self)

        self.setFixedSize(381, 470)

        self.go_btn.clicked.connect(self.gpa)
        self.add_btn.clicked.connect(self.add)
        self.exit_btn.clicked.connect(self.close)
        self.clear_btn.clicked.connect(self.clearFields)

    ## @brief Displays the 12.0 gpa from the metrics the user provides
    #  @details Takes in the grades and their weights through input fields and shows
    #  the users GPA result on the window
    def gpa(self):
        try:
            finalGPA = gpaCalculate(GPAWindow.gradeList, GPAWindow.totalWeight)

            self.lineEdit_3.setText(str(finalGPA))

        except ZeroDivisionError:
            self.clearFields()
            self.lineEdit_3.setText("Division By Zero!")

    ## @brief Sets up the visual aspect of the calculator and sets up inputs
    #  @details Takes in the grades and their weights through input fields and shows
    #  the users grades in the window as a tuple.
    def add(self):
        try:
            gradeRecieved = float(self.lineEdit.text())
            gradeWeight = float(self.lineEdit_2.text())

            gradeRecieved_2 = str(self.lineEdit.text())
            gradeWeight_2 = str(self.lineEdit_2.text())

            gradeAddView = "Grade: "+gradeRecieved_2+" Weight: "+gradeWeight_2

            gradeAddNum = gradeRecieved*gradeWeight

            GPAWindow.gradeList.append(gradeAddNum)
            self.listWidget.insertItem(GPAWindow.index,gradeAddView)
            GPAWindow.index += 1
            GPAWindow.totalWeight += gradeWeight

        except ValueError:
            self.clearFields()
            self.lineEdit_3.setText("Invalid Input!")

    ## @brief Closes window and clears inputs upon close
    def closeEvent(self, event):
        self.clearFields()
        event.accept()

    ## @brief Clears all input and output fields
    def clearFields(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.listWidget.clear()
        GPAWindow.gradeList.clear()
        GPAWindow.totalWeight = 0

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = GPAWindow()
    window.show()
    sys.exit(app.exec_())