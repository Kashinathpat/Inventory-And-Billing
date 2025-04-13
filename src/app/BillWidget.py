import sys

import qdarktheme
from PyQt6 import QtWidgets
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QHeaderView, QPushButton, QTableWidgetItem, QMessageBox

from src.ui.bill import Ui_BillWidget
from src.utils.database import mongo_client


class BillWidget(QtWidgets.QWidget, Ui_BillWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tableData: list[dict] = []
        self.listen()

    def showEvent(self, event):
        super().showEvent(event)
        self.loadData()
        self.setQuantity()
        self.initTable()

    def listen(self):
        self.productComboBox.currentIndexChanged.connect(self.setQuantity)
        self.addToBillButton.clicked.connect(self.addToBill)
        self.calculateBillButton.clicked.connect(self.calculateTotal)
        self.clearBillButton.clicked.connect(self.clearBill)

    def initTable(self):
        table_font = QFont("Segoe UI", 9)
        self.table.setFont(table_font)
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Product", "Quantity", "Price", "Total", "Delete"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def loadData(self):
        self.table.clear()
        self.tableData = mongo_client.get_inventory()
        if isinstance(self.tableData, str):
            QMessageBox.information(self, "Information", self.tableData)
            self.tableData = []
        self.productComboBox.clear()
        self.productComboBox.addItems([f"{data['name']} : {data['sku']}" for data in self.tableData])

    def setQuantity(self):
        selected = self.productComboBox.currentIndex()
        if selected == -1:
            return
        maxQuantity = int(self.tableData[selected]["stock"])
        if maxQuantity > 0:
            self.quantitySpinBox.setRange(1, maxQuantity)
            self.addToBillButton.setEnabled(True)
            self.addToBillButton.setText("Add To Bill")
        else:
            self.quantitySpinBox.setRange(0, 0)
            self.addToBillButton.setEnabled(False)
            self.addToBillButton.setText("Add To Bill(Disabled as selected product have no Stock available)")

    def addToBill(self):
        selected = self.productComboBox.currentIndex()
        data = self.tableData[selected]
        quantity = self.quantitySpinBox.value()
        data["stock"] -= quantity
        self.setQuantity()
        self.table.setRowCount(self.table.rowCount() + 1)

        name = data["name"]
        price = data["price"]
        total = quantity * price

        delete_btn = QPushButton("Delete")
        delete_btn.clicked.connect(lambda _, btn=delete_btn: self.deleteRow(btn))
        row = self.table.rowCount() - 1
        self.table.setItem(row, 0, QTableWidgetItem(name))
        self.table.setItem(row, 1, QTableWidgetItem(str(quantity)))
        self.table.setItem(row, 2, QTableWidgetItem(str(price)))
        self.table.setItem(row, 3, QTableWidgetItem(str(total)))
        self.table.setCellWidget(row, 4, delete_btn)

    def deleteRow(self, button):
        for row in range(self.table.rowCount()):
            if self.table.cellWidget(row, 4) == button:
                self.table.removeRow(row)
                break

    def calculateTotal(self):
        pass

    def clearBill(self):
        pass

def main():
    app = QApplication(sys.argv)
    qdarktheme.setup_theme("dark")
    window = BillWidget()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()