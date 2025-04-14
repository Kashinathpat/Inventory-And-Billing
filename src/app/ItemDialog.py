from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import QSettings
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
        self.settings = QSettings("inventory")
        self._font_size = self.settings.value("fontSize", 9)

        layout = QVBoxLayout()
        form = QFormLayout()

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
        self.fontSizeChange()
        self.setLayout(layout)

    def wheelEvent(self, event):
        if event.modifiers() == QtCore.Qt.KeyboardModifier.ControlModifier:
            delta = event.angleDelta().y()
            if delta > 0:
                self._font_size += 1
            else:
                self._font_size -= 1
            self._font_size = max(8, min(20, self._font_size))
            self.settings.setValue("fontSize", self._font_size)
            self.fontSizeChange()
            event.accept()
        else:
            super().wheelEvent(event)

    def fontSizeChange(self):
        self._font_size = self.settings.value("fontSize", 9)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(self._font_size)
        widgets = (
                self.findChildren(QtWidgets.QLabel) +
                self.findChildren(QtWidgets.QPushButton) +
                self.findChildren(QtWidgets.QLineEdit) +
                self.findChildren(QtWidgets.QSpinBox) +
                self.findChildren(QtWidgets.QDoubleSpinBox)
        )
        [widget.setFont(font) for widget in widgets]

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
            return
        self.accept()
