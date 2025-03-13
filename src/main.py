import sys
import qdarktheme
from src.ui.login import Ui_MainWindow
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication
import src.ui.res


class ProjectGUI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(ProjectGUI, self).__init__(*args, **kwargs)
        self.setupUi(self)


def main():
    app = QApplication(sys.argv)
    qdarktheme.setup_theme()
    window = ProjectGUI()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()