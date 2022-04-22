## @file algebra_ui.py
#  @brief Provides a class to display the Algebra window
#  @date March 30, 2022


from uis.slope_ui import SlopeWindow
from uis.y_int_ui import YintWindow
from uis.pythagore_ui import PythaWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi


## @brief AlgebraWindow is a class that implements the GUI components for the
#  Algebra operation menu

class AlgebraWindow(QMainWindow):

    ## @brief The constructor of the Algebra window
    #  @details Creates a pop up window that displays and sets up the buttons
    #  that are necessary to navigate from the Algebra window to other parts
    #  of the application.
    #  Also sets up the Algebra window according to the created style sheet.
    #  @param path The current path on which the file is found.
    #  Default value is an empty path.

    def __init__(self, path=""):
        super(AlgebraWindow, self).__init__()
        # Loading All the components needed

        self.path = f"{path}Ui_Base/algebra.ui"
        self.xpath = path
        loadUi(self.path, self)

        self.setFixedSize(658, 369)

        # Setting up the Windows needed
        self.slope1 = SlopeWindow(self.xpath)
        self.slope2 = YintWindow(self.xpath)
        self.pytha = PythaWindow(self.xpath)

        # Setting up the buttons functions
        self.slope_1.clicked.connect(self.slope1.show)
        self.slope_2.clicked.connect(self.slope2.show)
        self.pyth_btn.clicked.connect(self.pytha.show)
        self.exit_btn.clicked.connect(self.close)

    ## @brief Closes the window and any other algebra operation windows
    def closeEvent(self, event):
        self.slope1.close()
        self.slope2.close()
        self.pytha.close()
        event.accept()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = AlgebraWindow()
    window.show()
    sys.exit(app.exec_())
