# Form implementation generated from reading ui file '.\FirstDialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.btn_ok = QtWidgets.QPushButton(parent=Dialog)
        self.btn_ok.setGeometry(QtCore.QRect(40, 240, 75, 24))
        self.btn_ok.setObjectName("btn_ok")
        self.btn_cancel = QtWidgets.QPushButton(parent=Dialog)
        self.btn_cancel.setGeometry(QtCore.QRect(280, 240, 75, 24))
        self.btn_cancel.setObjectName("btn_cancel")
        self.lbl_title = QtWidgets.QLabel(parent=Dialog)
        self.lbl_title.setGeometry(QtCore.QRect(130, 80, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(True)
        self.lbl_title.setFont(font)
        self.lbl_title.setObjectName("lbl_title")
        self.lbl_invisible = QtWidgets.QLabel(parent=Dialog)
        self.lbl_invisible.setGeometry(QtCore.QRect(138, 166, 111, 41))
        self.lbl_invisible.setText("")
        self.lbl_invisible.setObjectName("lbl_invisible")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_ok.setText(_translate("Dialog", "OK"))
        self.btn_cancel.setText(_translate("Dialog", "Cancel"))
        self.lbl_title.setText(_translate("Dialog", "Presiona un Botón"))
