import sys

import qdarktheme
from PyQt6.QtWidgets import QApplication, QStackedWidget

from src.app.HomeGUI import HomeGUI
from src.app.LoginGUI import LoginGUI
import src.ui.res

class MainApp(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.login_window = LoginGUI(self)
        self.home_window = HomeGUI(self)
        self.addWidget(self.login_window)
        self.addWidget(self.home_window)
        self.setCurrentIndex(0)


def main():
    app = QApplication(sys.argv)
    qdarktheme.setup_theme("light")
    window = MainApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()