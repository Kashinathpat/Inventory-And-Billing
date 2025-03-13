from PyQt6.QtWidgets import QApplication, QWidget, QStackedWidget, QPushButton, QVBoxLayout, QLabel

class LoginWindow(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget  # Reference to QStackedWidget
        layout = QVBoxLayout()
        self.label = QLabel("Login Window")
        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.go_to_home)
        layout.addWidget(self.label)
        layout.addWidget(self.login_button)
        self.setLayout(layout)

    def go_to_home(self):
        self.stacked_widget.setCurrentIndex(1)  # Switch to Home Window

class HomeWindow(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Home Window")
        self.back_button = QPushButton("Logout")
        self.back_button.clicked.connect(lambda: stacked_widget.setCurrentIndex(0))  # Back to Login
        layout.addWidget(self.label)
        layout.addWidget(self.back_button)
        self.setLayout(layout)

class MainApp(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.login_window = LoginWindow(self)
        self.home_window = HomeWindow(self)
        self.addWidget(self.login_window)
        self.addWidget(self.home_window)
        self.setCurrentIndex(0)  # Start with Login Window

app = QApplication([])
main_app = MainApp()
main_app.show()
app.exec()
