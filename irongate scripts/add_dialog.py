# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\add_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import requests


class Ui_Dialog_Add(object):
    user_id = 0
    dialog = None
    pw = ''

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(401, 300)
        Dialog.setMinimumSize(QtCore.QSize(401, 300))
        Dialog.setMaximumSize(QtCore.QSize(401, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\images/irongate-icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setAutoFillBackground(False)
        self.background = QtWidgets.QLabel(Dialog)
        self.background.setGeometry(QtCore.QRect(0, -10, 411, 341))
        self.background.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.background.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(".\\images/background.png"))
        self.background.setObjectName("background")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(220, 270, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 270, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 81, 21))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 81, 21))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 121, 31))
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(100, 10, 291, 31))
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 50, 291, 31))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 90, 291, 31))
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 140, 81, 21))
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(100, 130, 291, 31))
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.warning = QtWidgets.QLabel(Dialog)
        self.warning.setGeometry(QtCore.QRect(10, 260, 211, 41))
        self.warning.setFont(font)
        self.warning.setAlignment(QtCore.Qt.AlignCenter)
        self.warning.setObjectName("warning")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 200, 381, 61))
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        Dialog.setModal(True)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.dialog = Dialog
        self.Handle_Buttons(Dialog)

    def Handle_Buttons(self, Dialog):
        self.pushButton_2.clicked.connect(Dialog.close)
        self.pushButton.clicked.connect(self.Add_Entity)


    def Add_Entity(self):
        name = self.lineEdit.text()
        username = self.lineEdit_2.text()
        self.warning.setText("")
        if 0< len(name) < 51 and 0 < len(username) < 33:
            password = self.lineEdit_3.text()
            if password == self.lineEdit_5.text() and 0 < len(password) < 33:
                notes = self.plainTextEdit.toPlainText()
                data = {
                    'name': name,
                    'username': username,
                    'password': password,
                    'notes': notes,
                    'user_id': self.user_id,
                    'pw': self.pw
                }
                requests.post('https://127.0.0.1:5000/addentity', verify=False, json=data)
                self.dialog.close()
            elif len(password) == 0:
                self.warning.setStyleSheet('QLabel {color: red;}')
                self.warning.setText("Password too short!")
            else:
                self.warning.setStyleSheet('QLabel {color: red;}')
                self.warning.setText("Passwords don't match!")
        elif len(name) > 51:
            self.warning.setStyleSheet('QLabel {color: red;}')
            self.warning.setText("Name too long!")
        elif len(name) == 0:
            self.warning.setStyleSheet('QLabel {color: red;}')
            self.warning.setText("Name too short!")
        elif len(username) == 0:
            self.warning.setStyleSheet('QLabel {color: red;}')
            self.warning.setText("Username too short!")
        else:
            self.warning.setStyleSheet('QLabel {color: red;}')
            self.warning.setText("Username too long!")


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "IronGate"))
        self.pushButton.setText(_translate("Dialog", "Add"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.label.setText(_translate("Dialog", "Name:"))
        self.label_2.setText(_translate("Dialog", "Username:"))
        self.label_3.setText(_translate("Dialog", "Password:"))
        self.label_4.setText(_translate("Dialog", "Notes(Optional):"))
        self.label_5.setText(_translate("Dialog", "Password:"))

