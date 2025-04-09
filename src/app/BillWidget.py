import sys

import qdarktheme
from PyQt6 import QtWidgets
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QHeaderView

from src.ui.bill import Ui_BillWidget


class BillWidget(QtWidgets.QWidget, Ui_BillWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.getTableData()

    def initTable(self):
        table_font = QFont("Segoe UI", 9)
        self.table.setFont(table_font)
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Product", "Quantity", "Price", "Total", "Delete"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def getTableData(self):
        self.table.clear()
        self.initTable()


def main():
    app = QApplication(sys.argv)
    qdarktheme.setup_theme("dark")
    window = BillWidget()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()