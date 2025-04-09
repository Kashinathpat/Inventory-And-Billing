import sys

import qdarktheme
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QStackedWidget, QHeaderView, QTableWidgetItem, QPushButton

from src.ui.home import Ui_HomeWindow
from src.utils.database import getInventoryData


class HomeGUI(QtWidgets.QMainWindow, Ui_HomeWindow):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.setupUi(self)
        self.stacked_widget.setWindowTitle("Home | Inventory and Billing")
        self.logoutPushButton.clicked.connect(self.logout)
        self.tableData = []
        self.initTable()
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)

    def showEvent(self, event):
        super().showEvent(event)
        self.getTableData()

    def initTable(self):
        self.addRecordButton.clicked.connect(self.add_row)
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["SKU", "Item Name", "Price", "Stock", "Update", "Delete"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def getTableData(self):
        self.tableData = getInventoryData()
        self.table.setRowCount(len(self.tableData))

        for row, val in enumerate(self.tableData):
            _id = val["_id"]
            name = val["name"]
            sku = val["sku"]
            price = val["price"]
            stock = val["stock"]

            update_btn = QPushButton("Update")
            delete_btn = QPushButton("Delete")
            update_btn.clicked.connect(lambda _, id=_id: self.update_row(id))
            delete_btn.clicked.connect(lambda _, id=_id: self.delete_row(id))

            self.table.setItem(row, 0, QTableWidgetItem(name))
            self.table.setItem(row, 1, QTableWidgetItem(sku))
            self.table.setItem(row, 2, QTableWidgetItem(str(price)))
            self.table.setItem(row, 3, QTableWidgetItem(str(stock)))
            self.table.setCellWidget(row, 4, update_btn)
            self.table.setCellWidget(row, 5, delete_btn)

    def logout(self):
        self.stacked_widget.setCurrentIndex(0)

    def add_row(self):
        pass

    def update_row(self, _id):
        pass

    def delete_row(self, _id):
        pass


def main():
    app = QApplication(sys.argv)
    qdarktheme.setup_theme("light")
    window = HomeGUI(QStackedWidget)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()