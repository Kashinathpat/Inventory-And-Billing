from PyQt6 import QtWidgets

from src.ui.login import Ui_MainWindow


class LoginGUI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.setupUi(self)
        self.loginPushButton.clicked.connect(self.login)

    def login(self):
        self.stacked_widget.setCurrentIndex(1)