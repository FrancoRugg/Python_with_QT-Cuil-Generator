# Form implementation generated from reading ui file '.\MainDniWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(683, 442)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_ok_ = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_ok_.setStyleSheet("QPushButton\n"
"{\n"
"color:whitesmoke;\n"
"background-color:rgb(202, 202, 202);\n"
"border:solid 1px black;\n"
"border-radius:3px; \n"
"border-style:hidden;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(86, 229, 78);\n"
"}")
        self.btn_ok_.setObjectName("btn_ok_")
        self.gridLayout.addWidget(self.btn_ok_, 2, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setStyleSheet("QLabel{\n"
"padding:0px;\n"
"}")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.cmb_Genre = QtWidgets.QComboBox(parent=self.centralwidget)
        self.cmb_Genre.setCurrentText("")
        self.cmb_Genre.setObjectName("cmb_Genre")
        self.verticalLayout.addWidget(self.cmb_Genre)
        self.line_dni = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.line_dni.setObjectName("line_dni")
        self.verticalLayout.addWidget(self.line_dni)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.lbl_invisible = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_invisible.setStyleSheet("QLabel{\n"
"background-color:grey;\n"
"color:white;\n"
"}")
        self.lbl_invisible.setText("")
        self.lbl_invisible.setObjectName("lbl_invisible")
        self.gridLayout.addWidget(self.lbl_invisible, 1, 0, 1, 1)
        self.btn_cancel_ = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_cancel_.setStyleSheet("QPushButton{\n"
"color:whitesmoke;\n"
"background-color:rgb(202, 202, 202);\n"
"border:solid 1px black;\n"
"border-radius:3px; \n"
"border-style:hidden;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:red;\n"
"}")
        self.btn_cancel_.setObjectName("btn_cancel_")
        self.gridLayout.addWidget(self.btn_cancel_, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 683, 22))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(parent=self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExportar = QtGui.QAction(parent=MainWindow)
        self.actionExportar.setObjectName("actionExportar")
        self.menuArchivo.addAction(self.actionExportar)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_ok_.setText(_translate("MainWindow", "OK"))
        self.label.setText(_translate("MainWindow", "Ingrese los datos solicitados"))
        self.cmb_Genre.setPlaceholderText(_translate("MainWindow", "Seleccionar Género:"))
        self.line_dni.setPlaceholderText(_translate("MainWindow", "Ingrese DNI:"))
        self.btn_cancel_.setText(_translate("MainWindow", "Cancel"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.actionExportar.setText(_translate("MainWindow", "Exportar"))
