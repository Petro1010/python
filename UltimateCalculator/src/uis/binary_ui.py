## @file binary_ui.py
#  @brief Provides a class to display the Binary window
#  @date March 18, 2022

from uis.floating_point_ui import FloatingPointWindow
from uis.binary_arithmetic_ui import BinArithmeticWindow
from uis.bitwise_ui import BitwiseWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi

## @brief BinaryWindow is a class that implements the GUI components for the Binary operation menu

class BinaryWindow(QMainWindow):

    ## @brief The constructor of the Binary window
    #  @details Creates a pop up window that displays and sets up the buttons that are
    #  necessary to navigate from the Binary window to other parts of the application.
    #  Also sets up the Binary window according to the created style sheet.
    #  @param path The current path on which the file is found. Default value is an empty path.
    def __init__(self, path=""):
        super(BinaryWindow, self).__init__()

        self.path = f"{path}Ui_Base/binary.ui"
        self.xpath = path
        loadUi(self.path, self)

        self.fp = FloatingPointWindow(self.xpath)
        self.ba = BinArithmeticWindow(self.xpath)
        self.bw = BitwiseWindow(self.xpath)
        
        self.floatingPoint.clicked.connect(self.fp.show)
        self.binArithmetic.clicked.connect(self.ba.show)
        self.bitwise.clicked.connect(self.bw.show)
        self.exit_btn.clicked.connect(self.close)

    ## @brief Closes the window and any other geometry operation windows
    def closeEvent(self, event):
        self.fp.close()
        self.ba.close()
        self.bw.close()
        event.accept()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = BinaryWindow()
    window.show()
    sys.exit(app.exec_())       

