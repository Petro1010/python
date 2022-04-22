## @file health_ui.py
#  @brief Provides a class to display the Health window
#  @date March 30, 2022


from uis.BMI_ui import BMIWindow
from uis.BodyFat_ui import BFWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi


## @brief HealthWindow is a class that implements the GUI components
#  for the Health operation menu

class HealthWindow(QMainWindow):

    ## @brief The constructor of the Health window
    #  @details Creates a pop up window that displays and sets up the
    #  buttons that are necessary to navigate from the Health window
    #  to other parts of the application. Also sets up the Health window
    #  according to the created style sheet.
    #  @param path The current path on which the file is found.
    #  Default value is an empty path.

    def __init__(self, path=""):
        super(HealthWindow, self).__init__()
        # Loading All the components needed

        self.path = f"{path}Ui_Base/health.ui"
        self.xpath = path
        loadUi(self.path, self)

        self.setFixedSize(658, 369)

        # Setting up the Windows needed
        self.bmi = BMIWindow(self.xpath)
        self.bf = BFWindow(self.xpath)

        # Setting up the buttons functions
        self.bmi_btn.clicked.connect(self.bmi.show)
        self.bf_btn.clicked.connect(self.bf.show)
        self.exit_btn.clicked.connect(self.hide)

    ## @brief Closes the window and any other health operation windows
    def closeEvent(self, event):
        self.bf.close()
        self.bmi.close()
        event.accept()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = HealthWindow()
    window.show()
    sys.exit(app.exec_())
