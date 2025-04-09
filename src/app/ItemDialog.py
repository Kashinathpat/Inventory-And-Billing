from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QFormLayout,
    QLineEdit, QPushButton, QHBoxLayout
)

class ItemDialog(QDialog):
    def __init__(self, parent=None, initial_data=None, is_update=False):
        super().__init__(parent)

        self.setWindowTitle("Update Item" if is_update else "Add New Item")
        self.setMinimumWidth(300)

        layout = QVBoxLayout()
        form = QFormLayout()

        self.name_input = QLineEdit()
        self.sku_input = QLineEdit()
        self.price_input = QLineEdit()
        self.stock_input = QLineEdit()

        if initial_data:
            self.name_input.setText(initial_data.get("name", ""))
            self.sku_input.setText(initial_data.get("sku", ""))
            self.price_input.setText(str(initial_data.get("price", "")))
            self.stock_input.setText(str(initial_data.get("stock", "")))

        form.addRow("Name:", self.name_input)
        form.addRow("SKU:", self.sku_input)
        form.addRow("Price:", self.price_input)
        form.addRow("Stock:", self.stock_input)

        layout.addLayout(form)

        button_layout = QHBoxLayout()
        self.confirm_button = QPushButton("Update" if is_update else "Add")
        self.cancel_button = QPushButton("Cancel")

        self.confirm_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

        button_layout.addWidget(self.cancel_button)
        button_layout.addWidget(self.confirm_button)
        self.confirm_button.setDefault(True)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def get_data(self):
        return {
            "name": self.name_input.text(),
            "sku": self.sku_input.text(),
            "price": self.price_input.text(),
            "stock": self.stock_input.text(),
        }
