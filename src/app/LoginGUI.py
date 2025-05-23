from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox

from src.ui.login import Ui_MainWindow
from src.utils.database import mongo_client


class LoginGUI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.setupUi(self)
        self.loginPushButton.clicked.connect(self.login)
        self.userline.setText(self.stacked_widget.settings.value("username", ''))

    def showEvent(self, event):
        super().showEvent(event)
        self.stacked_widget.setWindowTitle("Login | Inventory and Billing")

    def login(self) -> None:
        user = self.userline.text()
        passwd = self.passline.text()

        res = mongo_client.check_login(user, passwd)
        if not res:
            self.passline.setText("")
            self.stacked_widget.settings.setValue("username", user)
            self.stacked_widget.setCurrentIndex(1)
        else:
            QMessageBox.information(self, "Information", str(res))