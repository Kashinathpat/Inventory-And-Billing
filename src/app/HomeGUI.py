from PyQt6 import QtWidgets

from src.ui.home import Ui_HomeWindow


class HomeGUI(QtWidgets.QMainWindow, Ui_HomeWindow):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.setupUi(self)
        self.logoutPushButton.clicked.connect(self.logout)

    def logout(self):
        self.stacked_widget.setCurrentIndex(0)