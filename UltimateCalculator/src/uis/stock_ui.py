## @file stock_ui.py
#  @brief Provides a class to display the Stocks window
#  @date March 17, 2022

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from uis.Calculators.stocks_calculator import calcUserGainLossCase1, calcUserGainLossCase2

## @brief StockWindow is a class that implements the GUI components for the Stock operation menu


class StockWindow(QMainWindow):

    ## @brief The constructor of the Stock window
    #  @details Creates a pop up window that displays and sets up the buttons that are
    #  necessary to navigate from the Stocks window to other parts of the application.
    #  Also sets up the Stocks window according to the created style sheet.
    #  @param path The current path on which the file is found. Default value is an empty path.

    def __init__(self, path=""):
        super(StockWindow, self).__init__()

        self.path = f"{path}Ui_Base/stock.ui"
        loadUi(self.path, self)

        self.setFixedSize(397, 564)

        self.go_btn.clicked.connect(self.stock)
        self.exit_btn.clicked.connect(self.close)
        self.clear_btn.clicked.connect(self.clearFields)

    ## @brief Displays the loss or gain on the stock from the metrics the user provides
    #  @details Takes in the number of shares, purchase price, sell price, purchase commission
    #  and sell commission, through input fields, and shows the user the result on the window

    def stock(self):

        try:
            user_shares = float(self.lineEdit.text())
            user_purchase_price = float(self.lineEdit_2.text())
            user_sell_price = float(self.lineEdit_3.text())
            try:
                user_buy_commission = float(self.lineEdit_4.text())
                user_sell_commission = float(self.lineEdit_5.text())
                user_gain_loss = calcUserGainLossCase1(user_shares,user_purchase_price,user_sell_price,user_buy_commission,user_sell_commission)
                self.lineEdit_6.setText(str(user_gain_loss))
            except ValueError:
                self.clearFields()
                self.lineEdit_6.setText("Invalid Input!")
            except:
                user_gain_loss = calcUserGainLossCase2(user_shares,user_purchase_price,user_sell_price)
                self.lineEdit_6.setText(str(user_gain_loss))

        except ValueError:
            self.clearFields()
            self.lineEdit_6.setText("Invalid Input!")

    ## @brief Closes window and clears inputs upon close
    def closeEvent(self, event):
        self.clearFields()
        event.accept()

    ## @brief Clears all input and output fields
    def clearFields(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        self.lineEdit_6.setText("")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = StockWindow()
    window.show()
    sys.exit(app.exec_())
