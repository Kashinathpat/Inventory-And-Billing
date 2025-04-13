import sys

import qdarktheme
from PyQt6 import QtWidgets
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QStackedWidget, QHeaderView, QTableWidgetItem, QPushButton, QMessageBox

from src.app.BillWidget import BillWidget
from src.app.ItemDialog import ItemDialog
from src.ui.home import Ui_HomeWindow
from src.utils.database import mongo_client


class HomeGUI(QtWidgets.QMainWindow, Ui_HomeWindow):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.setupUi(self)
        self.logoutPushButton.clicked.connect(self.logout)
        self.tableData = []
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.addRecordButton.clicked.connect(self.add_row)
        layout = self.tabWidget.widget(1).layout()
        layout.addWidget(BillWidget())
        self.tabWidget.setCurrentIndex(1)

    def showEvent(self, event):
        super().showEvent(event)
        self.stacked_widget.setWindowTitle("Home | Inventory and Billing")
        self.getTableData()

    def alert(self, text: str) -> None:
        QMessageBox.information(self, "Information", text)

    def initTable(self):
        table_font = QFont("Segoe UI", 9)
        self.table.setFont(table_font)
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["SKU", "Item Name", "Price", "Stock", "Update", "Delete"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def getTableData(self):
        self.table.clear()
        self.initTable()
        self.tableData = mongo_client.get_inventory()
        if isinstance(self.tableData, str):
            self.alert(self.tableData)
            self.tableData = []
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

    def confirm_action(self):
        reply = QMessageBox.question(
            self,
            "Confirm",
            "Are you sure you want to proceed?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        return reply == QMessageBox.StandardButton.Yes

    def add_row(self):
        dialog = ItemDialog(self)
        if dialog.exec() and not dialog.operation:
            self.getTableData()

    def update_row(self, _id):
        data = [item for item in self.tableData if item["_id"] == _id][0]

        dialog = ItemDialog(self, initial_data=data, is_update=True)
        if dialog.exec() and not dialog.operation:
            self.getTableData()

    def delete_row(self, _id):
        if self.confirm_action():
            mongo_client.deleteItem(_id)
            self.getTableData()


def main():
    app = QApplication(sys.argv)
    qdarktheme.setup_theme("light")
    window = HomeGUI(QStackedWidget)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()