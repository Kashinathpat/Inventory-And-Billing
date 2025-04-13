from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QFormLayout,
    QLineEdit, QPushButton, QHBoxLayout,
    QSpinBox, QDoubleSpinBox
)
from src.utils.database import mongo_client

class ItemDialog(QDialog):
    def __init__(self, parent=None, initial_data=None, is_update=False):
        super().__init__(parent)

        self.setWindowTitle("Update Item" if is_update else "Add New Item")
        self.setMinimumWidth(300)

        layout = QVBoxLayout()
        form = QFormLayout()

        self.operation = False
        self.is_update = is_update
        self._id = ""
        self.name_input = QLineEdit()
        self.sku_input = QLineEdit()
        self.price_input = QDoubleSpinBox()
        self.stock_input = QSpinBox()

        self.price_input.setRange(1.00, 999999.99)
        self.price_input.setDecimals(2)
        self.price_input.setSingleStep(0.10)
        self.stock_input.setRange(0, 100000)

        if initial_data:
            self._id = initial_data.get("_id", "")
            self.name_input.setText(initial_data.get("name", ""))
            self.sku_input.setText(initial_data.get("sku", ""))
            self.price_input.setValue(float(initial_data.get("price", 1.0)))
            self.stock_input.setValue(int(initial_data.get("stock", 0)))

        form.addRow("Name:", self.name_input)
        form.addRow("SKU:", self.sku_input)
        form.addRow("Price:", self.price_input)
        form.addRow("Stock:", self.stock_input)

        layout.addLayout(form)

        button_layout = QHBoxLayout()
        self.confirm_button = QPushButton("Update" if is_update else "Add")
        self.cancel_button = QPushButton("Cancel")

        self.confirm_button.clicked.connect(self.onSubmit)
        self.cancel_button.clicked.connect(self.reject)

        button_layout.addWidget(self.cancel_button)
        button_layout.addWidget(self.confirm_button)
        self.confirm_button.setDefault(True)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def onSubmit(self):
        name = self.name_input.text().strip()
        sku = self.sku_input.text().strip()
        price = self.price_input.value()
        stock = self.stock_input.value()

        if not name or not sku:
            self.parent().alert("Name and SKU cannot be empty.")
            return

        if self.is_update:
            msg = mongo_client.updateItem(self._id, name, sku, price, stock)
        else:
            msg = mongo_client.addItem(name, sku, price, stock)

        if msg != "":
            self.parent().alert(msg)
        self.operation = True
        self.accept()
