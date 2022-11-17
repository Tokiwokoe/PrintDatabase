# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddClient.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(740, 140)
        Dialog.setStyleSheet("background-color: rgb(245, 245, 175)")
        self.name = QtWidgets.QLineEdit(Dialog)
        self.name.setGeometry(QtCore.QRect(10, 40, 231, 20))
        self.name.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.name.setText("")
        self.name.setObjectName("name")
        self.dateEdit = QtWidgets.QDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(250, 40, 110, 22))
        self.dateEdit.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.dateEdit.setObjectName("dateEdit")
        self.phone = QtWidgets.QLineEdit(Dialog)
        self.phone.setGeometry(QtCore.QRect(372, 40, 141, 20))
        self.phone.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.phone.setText("")
        self.phone.setObjectName("phone")
        self.addres = QtWidgets.QLineEdit(Dialog)
        self.addres.setGeometry(QtCore.QRect(520, 40, 211, 20))
        self.addres.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.addres.setText("")
        self.addres.setObjectName("addres")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 231, 20))
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"font-size: 16px;\n"
"font: \"Arial Black\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(250, 10, 111, 20))
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);\n"
"font-size: 16px;\n"
"font: \"Arial Black\";")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(370, 10, 141, 20))
        self.label_7.setStyleSheet("color: rgb(0, 0, 0);\n"
"font-size: 16px;\n"
"font: \"Arial Black\";")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(520, 10, 211, 20))
        self.label_8.setStyleSheet("color: rgb(0, 0, 0);\n"
"font-size: 16px;\n"
"font: \"Arial Black\";")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.OKbutton = QtWidgets.QPushButton(Dialog)
        self.OKbutton.setGeometry(QtCore.QRect(570, 90, 161, 41))
        self.OKbutton.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.OKbutton.setObjectName("OKbutton")
        self.error = QtWidgets.QLabel(Dialog)
        self.error.setGeometry(QtCore.QRect(10, 100, 541, 21))
        self.error.setStyleSheet("color: red;\n"
"font-size: 16px;\n"
"font: 16pt \"Franklin Gothic Demi\";")
        self.error.setText("")
        self.error.setAlignment(QtCore.Qt.AlignCenter)
        self.error.setObjectName("error")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "ФИО"))
        self.label_5.setText(_translate("Dialog", "Дата рождения"))
        self.label_7.setText(_translate("Dialog", "Телефон"))
        self.label_8.setText(_translate("Dialog", "Адрес"))
        self.OKbutton.setText(_translate("Dialog", "ОК"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())