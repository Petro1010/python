## @file conversion_ui.py
#  @brief Provides a class to display the Conversion window
#  @date March 17, 2022


from uis.ConversionCurrency_ui import ConversionCurrencyWindow
from uis.ConversionCrypto_ui import ConversionCryptoWindow
from uis.ConversionBase_ui import ConversionBaseWindow
from uis.ConversionRN_ui import ConversionRNWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi


## @brief ConverterWindow is a class that implements the GUI components for the Conversion operation menu

class ConverterWindow(QMainWindow):

    ## @brief The constructor of the Conversion window
    #  @details Creates a pop up window that displays and sets up the buttons that are
    #  necessary to navigate from the Conversion window to other parts of the application.
    #  Also sets up the Conversion window according to the created style sheet.
    #  @param path The current path on which the file is found. Default value is an empty path.

    def __init__(self, path=""):
        super(ConverterWindow, self).__init__()
        # Loading All the components needed

        self.path = f"{path}Ui_Base/conversion.ui"
        self.xpath = path
        loadUi(self.path, self)

        self.setFixedSize(643, 441)


        # Setting up the Windows needed
        self.currency = ConversionCurrencyWindow(self.xpath)
        self.base = ConversionBaseWindow(self.xpath)
        self.crypto = ConversionCryptoWindow(self.xpath)
        self.RN = ConversionRNWindow(self.xpath)

        # Setting up the buttons functions
        self.curr_btn.clicked.connect(self.currency.show)
        self.crypto_btn.clicked.connect(self.crypto.show)
        self.base_btn.clicked.connect(self.base.show)
        self.rn_btn.clicked.connect(self.RN.show)
        self.exit_btn.clicked.connect(self.close)

    ## @brief Closes the window and any other algebra operation windows
    def closeEvent(self, event):
        self.currency.close()
        self.base.close()
        self.crypto.close()
        self.RN.close()
        event.accept()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = ConverterWindow()
    window.show()
    sys.exit(app.exec_())
