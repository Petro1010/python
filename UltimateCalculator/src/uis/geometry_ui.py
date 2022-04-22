## @file geometry_ui.py
#  @brief Provides a class to display the Geometry window
#  @date March 18, 2022

from uis.area_ui import AreaWindow
from uis.perimeter_ui import PerimeterWindow
from uis.volume_ui import VolumeWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi

## @brief GeometryWindow is a class that implements the GUI components for the Geometry operation menu

class GeometryWindow(QMainWindow):

    ## @brief The constructor of the Geometry window
    #  @details Creates a pop up window that displays and sets up the buttons that are
    #  necessary to navigate from the Geometry window to other parts of the application.
    #  Also sets up the Geometry window according to the created style sheet.
    #  @param path The current path on which the file is found. Default value is an empty path.
    def __init__(self, path=""):
        super(GeometryWindow, self).__init__()

        self.path = f"{path}Ui_Base/geometry.ui"
        self.xpath = path
        loadUi(self.path, self)

        self.setFixedSize(658, 369)

        self.a = AreaWindow(self.xpath)
        self.p = PerimeterWindow(self.xpath)
        self.v = VolumeWindow(self.xpath)
        
        self.area.clicked.connect(self.a.show)
        self.perimeter.clicked.connect(self.p.show)
        self.volume.clicked.connect(self.v.show)
        self.exit_btn.clicked.connect(self.close)

    ## @brief Closes the window and any other geometry operation windows
    def closeEvent(self, event):
        self.a.close()
        self.p.close()
        self.v.close()
        event.accept()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = GeometryWindow()
    window.show()
    sys.exit(app.exec_())       

