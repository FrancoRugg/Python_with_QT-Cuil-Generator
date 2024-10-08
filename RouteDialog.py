# Form implementation generated from reading ui file '.\RouteDialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(417, 405)
        Dialog.setStyleSheet("QDialog{\n"
"background-color:whitesmoke;\n"
"border:solid 2px black;\n"
"border-radius:4px;\n"
"}")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_route = QtWidgets.QLabel(parent=Dialog)
        self.label_route.setObjectName("label_route")
        self.verticalLayout.addWidget(self.label_route)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.line_route = QtWidgets.QLineEdit(parent=Dialog)
        self.line_route.setObjectName("line_route")
        self.verticalLayout_4.addWidget(self.line_route)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_ok_route = QtWidgets.QPushButton(parent=Dialog)
        self.btn_ok_route.setStyleSheet("QPushButton\n"
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
        self.btn_ok_route.setObjectName("btn_ok_route")
        self.verticalLayout_2.addWidget(self.btn_ok_route)
        self.btn_cancel_route = QtWidgets.QPushButton(parent=Dialog)
        self.btn_cancel_route.setStyleSheet("QPushButton{\n"
"color:whitesmoke;\n"
"background-color:rgb(202, 202, 202);\n"
"border:solid 1px black;\n"
"border-radius:3px; \n"
"border-style:hidden;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:red;\n"
"}")
        self.btn_cancel_route.setObjectName("btn_cancel_route")
        self.verticalLayout_2.addWidget(self.btn_cancel_route)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_route.setText(_translate("Dialog", "Ingresar ruta:"))
        self.line_route.setPlaceholderText(_translate("Dialog", "/routa"))
        self.btn_ok_route.setText(_translate("Dialog", "OK"))
        self.btn_cancel_route.setText(_translate("Dialog", "Cancel"))
