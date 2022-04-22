## @file ConversionCrypto_ui.py
#  @brief Provides a class to display the crypto conversion window
#  @date March 18, 2022

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from uis.Calculators.conversion_calculator import convertCrypto

## @brief ConversionCryptoWindow is a class that implements the GUI components for the crypto conversion operation

class ConversionCryptoWindow(QMainWindow):

    ## @brief The constructor of the crypto conversion window
    #  @details Creates a pop up window that displays and sets up the buttons and input fields that are
    #  necessary to obtain input from the user and calculate the appropriate answer.
    #  Also sets up the window according to the created style sheet.
    #  @param path The current path on which the file is found. Default value is an empty path.
    def __init__(self, path=""):
        super(ConversionCryptoWindow, self).__init__()

        self.path = f"{path}Ui_Base/conversionCrypto.ui"
        loadUi(self.path, self)

        self.setFixedSize(421, 485)

        self.cvt_btn.clicked.connect(self.cryptoconvert)
        self.exit_btn.clicked.connect(self.close)
        self.clear_btn.clicked.connect(self.clearFields)

    ## @brief Displays the conversion a value of a base type 1 to a value of base type 2
    #  @details Takes in 1 value and the convert to and convert from type as input from the user through input
    #  fields and shows the user the result on the window
    def cryptoconvert(self):
        try:
            initialVal = (self.line1.text())
            currFrom = (self.comboBox1.currentText())
            currTo = (self.comboBox2.currentText())

            conversion = convertCrypto(initialVal, currFrom, currTo)
            self.line2.setText(str(conversion))
        except:
            self.line2.setText("Invalid Input")

        ## @brief Closes window and clears inputs upon close
    def closeEvent(self, event):
        self.clearFields()
        event.accept()

    ## @brief Clears all input and output fields
    def clearFields(self):
        self.line1.setText("")
        self.comboBox1.setCurrentIndex(0)
        self.comboBox2.setCurrentIndex(0)
        self.line2.setText("")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = ConversionCryptoWindow()
    window.show()
    sys.exit(app.exec_())
