## @file main.py
#  @brief Provides a class to display the Main window
#  @date March 30, 2022

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from uis.Conversion_ui import ConverterWindow
from uis.algebra_ui import AlgebraWindow
from uis.stock_ui import StockWindow
from uis.health_ui import HealthWindow
from uis.gpa_ui import GPAWindow
from uis.geometry_ui import GeometryWindow
from uis.binary_ui import BinaryWindow
from uis.Calculators.main_calculator import Calculator
import webbrowser
from sys import exit

from uis.MainWindow import Ui_MainWindow

## @brief MainWindow is a class that implements the GUI components for the Main menu

class MainWindow(QMainWindow, Ui_MainWindow):

    ## @brief The constructor of the Main window
    #  @details Creates a pop up window that displays and sets up the buttons that are
    #  necessary to navigate from the Main window to other parts of the application.
    #  Also sets up the Main window according to the created style sheet.
    #  @param path The current path on which the file is found. Default value is an empty path.  


    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # Loading All the components needed

        self.setupUi(self)

        self.setFixedSize(417, 787)

        # Setting up the Windows needed

        self.converters = ConverterWindow("uis/")
        self.algebra = AlgebraWindow("uis/")
        self.stock = StockWindow("uis/")
        self.health = HealthWindow("uis/")
        self.gpa = GPAWindow("uis/")
        self.binary = BinaryWindow("uis/")
        self.geo = GeometryWindow("uis/")

        # Setting up the buttons functions
        self.calc = Calculator()

        self.pushButton_stock.clicked.connect(self.stock.show)
        self.pushButton_convert.clicked.connect(self.converters.show)
        self.pushButton_alg.clicked.connect(self.algebra.show)
        self.pushButton_credits.clicked.connect(self.credits)
        self.pushButton_health.clicked.connect(self.health.show)
        self.pushButton_gpa.clicked.connect(self.gpa.show)
        self.pushButton_geo.clicked.connect(self.geo.show)
        self.pushButton_bin.clicked.connect(self.binary.show)

        self.pushButton_add.clicked.connect(self.addition)
        self.pushButton_sub.clicked.connect(self.subtraction)
        self.pushButton_mul.clicked.connect(self.multiplication)
        self.pushButton_div.clicked.connect(self.division)
        self.pushButton_eq.clicked.connect(self.equals)

        self.pushButton_ac.clicked.connect(self.reset)
        
        self.pushButton_m.pressed.connect(self.storeMem)
        self.pushButton_mr.pressed.connect(self.getMem)
        self.pushButton_pc.pressed.connect(lambda v=".": self.valueInput(v))
        self.pushButton_n0.pressed.connect(lambda v="0": self.valueInput(v))
        self.pushButton_n1.pressed.connect(lambda v="1": self.valueInput(v))
        self.pushButton_n2.pressed.connect(lambda v="2": self.valueInput(v))
        self.pushButton_n3.pressed.connect(lambda v="3": self.valueInput(v))
        self.pushButton_n4.pressed.connect(lambda v="4": self.valueInput(v))
        self.pushButton_n5.pressed.connect(lambda v="5": self.valueInput(v))
        self.pushButton_n6.pressed.connect(lambda v="6": self.valueInput(v))
        self.pushButton_n7.pressed.connect(lambda v="7": self.valueInput(v))
        self.pushButton_n8.pressed.connect(lambda v="8": self.valueInput(v))
        self.pushButton_n9.pressed.connect(lambda v="9": self.valueInput(v))
        self.display()
        self.show()

    ## @brief Stores the current number
    #  @details stores number for future use
    def storeMem(self):
        self.calc.storeMem()
    
    ## @brief Displays current stored number
    #  @details Checks if current stored number is empty and adds new number number to store and display
    def getMem(self):
        self.calc.getMem()
        self.display()

    ## @brief Displays number to user
    #  @details displays the number that is currently stored onto the calculator display
    def display(self):
        self.lcdNumber.display(self.calc.getCurrNum())

    ## @brief Displays error message
    def displayError(self):
        self.lcdNumber.display("Error")

    ## @brief Display value of input
    #  @details Adds the input v to the value of current number and displays it
    def valueInput(self, v):
        self.calc.valueInput(v)
        self.display()

    ## @brief Empty the line and current number stored
    #  @details Clears the line value and the current number value to an empty string value and display new blank value
    def reset(self):
        self.calc.reset()
        self.display()

    ## @brief Conducts calculator addition operation
    #  @details Check if line input prior is not another operation and if it is not, display an empty string and adds an addition operation
    def addition(self):
        self.calc.addition()
        self.display()

    ## @brief Conducts calculator subtraction operation
    #  @details Check if line input prior is not another operation and if it is not, display an empty string and adds a subtraction operation
    def subtraction(self):
        self.calc.subtraction()
        self.display()

    ## @brief Conducts calculator multiplication operation
    #  @details Check if line input prior is not another operation and if it is not, display an empty string and adds a multiplication operation
    def multiplication(self):
        self.calc.multiplication()
        self.display()

    ## @brief Conducts calculator power operation
    #  @details Check if line input prior is not another operation and if it is not, display an empty string and adds a power operation
    def power(self):
        self.calc.power()
        self.display()

    ## @brief Conducts calculator division operation
    #  @details Check if line input prior is not another operation and if it is not, display an empty string and adds a division operation
    def division(self):
        self.calc.division()
        self.display()

    ## @brief Adds left bracket operation
    #  @details Clears the display and adds a left bracket to the operation
    def left_bracket(self):
        self.calc.left_bracket()
        self.display()

    ## @brief Adds right bracket operation
    #  @details Clears the display and adds a right bracket to the operation
    def right_bracket(self):
        self.calc.right_bracket()
        self.display()

    ## @brief Evaluates operation 
    #  @details Evaluates operation and displays answer
    def equals(self):
        #calculation = self.lineEdit
        try:
            self.calc.evaluate()
            self.display()
        except:
            self.displayError()
            self.calc.reset()

    ## @brief Runs functionality for each button click in the calculator
    #  @details Hooks up the calculator button presses to the functions adding them to the operation
    def keyPressEvent(self, event):
        key = event.text()
        if key in [str(i) for i in range(10)]:
            self.calc.valueInput(key)
            self.display()

        elif key == "+":
            self.addition()

        elif key == "-":
            self.subtraction()

        elif key in ["*", "x"]:
            self.multiplication()

        elif key == "/":
            self.division()

        elif key == "=":
            self.equals()

        elif key == ".":
            self.calc.valueInput(".")
            self.display()

        elif key == "(":
            self.left_bracket()

        elif key == ")":
            self.right_bracket()

        elif key == "^":
            self.power()
        
        elif key == "c":
            self.reset()
        
        elif key == "m":
            self.storeMem()
        
        elif key == "r":
            self.getMem()

        elif event.key() == 16777219:  # Key Code for Backspace
            self.calc.delete()
            self.display()

        elif event.key() == 16777220:  # Key Code for Enter
            self.equals()
    
    ## @brief Closes the window and any other open windows
    #  upon confirmation
    def closeEvent(self, event):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setText("Are you sure you want to quit?")
        msg.setWindowTitle("Quit")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        reply = msg.exec()
        if reply == QMessageBox.Yes:
            self.converters.close()
            self.algebra.close()
            self.stock.close()
            self.health.close()
            self.gpa.close()
            self.binary.close()
            self.geo.close()
            event.accept()
        else:
            event.ignore()
        
    @staticmethod
    def credits():
        webbrowser.open_new(
            "https://gitlab.cas.mcmaster.ca/petronim/ultimate_calculator_l01_group15")

def start_gui():
    app = QApplication([])
    app.setApplicationName("PyQt Calculator")

    window = MainWindow()
    app.exec_()

if __name__ == '__main__':
    start_gui()
