import sys

import qdarktheme
from PyQt6 import QtWidgets
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QHeaderView

from src.ui.bill import Ui_BillWidget
from src.utils.database import getInventoryData


class BillWidget(QtWidgets.QWidget, Ui_BillWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tableData: list[dict] = []
        self.loadData()
        self.setQuantity()
        self.initTable()
        self.listen()

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
        self.tableData = getInventoryData()
        self.productComboBox.clear()
        self.productComboBox.addItems([f"{data['name']} : {data['sku']}" for data in self.tableData])

    def setQuantity(self):
        selected = self.productComboBox.currentIndex()
        maxQuantity = self.tableData[selected]["stock"]
        self.quantitySpinBox.setMaximum(maxQuantity)

    def addToBill(self):
        pass

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