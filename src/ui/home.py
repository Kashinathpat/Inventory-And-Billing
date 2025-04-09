# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_HomeWindow(object):
    def setupUi(self, HomeWindow):
        HomeWindow.setObjectName("HomeWindow")
        HomeWindow.resize(806, 467)
        self.centralwidget = QtWidgets.QWidget(parent=HomeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabWidget::tab-bar {\n"
"    alignment: center;\n"
"}\n"
"QTabBar::tab {\n"
"    padding: 12px 25px; \n"
"}")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.TabPosition.North)
        self.tabWidget.setObjectName("tabWidget")
        self.inventoryTab = QtWidgets.QWidget()
        self.inventoryTab.setObjectName("inventoryTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.inventoryTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.addRecordButton = QtWidgets.QPushButton(parent=self.inventoryTab)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.addRecordButton.setFont(font)
        self.addRecordButton.setObjectName("addRecordButton")
        self.horizontalLayout.addWidget(self.addRecordButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.table = QtWidgets.QTableWidget(parent=self.inventoryTab)
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.verticalLayout_2.addWidget(self.table)
        self.tabWidget.addTab(self.inventoryTab, "")
        self.billingTab = QtWidgets.QWidget()
        self.billingTab.setObjectName("billingTab")
        self.tabWidget.addTab(self.billingTab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.logoutPushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.logoutPushButton.setMinimumSize(QtCore.QSize(83, 36))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.logoutPushButton.setFont(font)
        self.logoutPushButton.setObjectName("logoutPushButton")
        self.horizontalLayout_2.addWidget(self.logoutPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        HomeWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(HomeWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(HomeWindow)

    def retranslateUi(self, HomeWindow):
        _translate = QtCore.QCoreApplication.translate
        HomeWindow.setWindowTitle(_translate("HomeWindow", "Home"))
        self.addRecordButton.setText(_translate("HomeWindow", "Add Item"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.inventoryTab), _translate("HomeWindow", "Inventory"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.billingTab), _translate("HomeWindow", "Billing"))
        self.logoutPushButton.setText(_translate("HomeWindow", "Log Out"))
