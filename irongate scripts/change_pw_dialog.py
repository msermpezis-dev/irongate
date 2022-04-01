# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\change_pw_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from pw_strength import PasswordStats
from email_plus import Email
import requests
import re
import time


class Ui_change_pw_Dialog(object):
    mp = ''
    email = ''

    def setupUi(self, change_pw_Dialog):
        change_pw_Dialog.setObjectName("change_pw_Dialog")
        change_pw_Dialog.resize(400, 280)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(change_pw_Dialog.sizePolicy().hasHeightForWidth())
        change_pw_Dialog.setSizePolicy(sizePolicy)
        change_pw_Dialog.setMinimumSize(QtCore.QSize(400, 280))
        change_pw_Dialog.setMaximumSize(QtCore.QSize(400, 280))
        change_pw_Dialog.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\images/irongate-icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        change_pw_Dialog.setWindowIcon(icon)
        self.tabWidget = QtWidgets.QTabWidget(change_pw_Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, -20, 411, 311))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(200, 240, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 240, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 321, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFont(font)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 110, 371, 111))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setFont(font)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 20, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(10, 240, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(0, 20, 411, 301))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(".\\images/light-background-small.png"))
        self.label_8.setObjectName("label_8")
        self.label_8.raise_()
        self.plainTextEdit.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.label_2.raise_()
        self.lineEdit.raise_()
        self.label.raise_()
        self.label_6.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 60, 361, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setFont(font)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 120, 361, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setFont(font)
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(20, 40, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(220, 40, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(240, 100, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 240, 111, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(300, 240, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(0, 20, 411, 301))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(".\\images/light-background-small.png"))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(130, 180, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(150, 240, 101, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.progressBar = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar.setGeometry(QtCore.QRect(160, 190, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_9.raise_()
        self.pushButton_3.raise_()
        self.lineEdit_2.raise_()
        self.label_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.label_4.raise_()
        self.lineEdit_3.raise_()
        self.label_5.raise_()
        self.label_7.raise_()
        self.label_10.raise_()
        self.progressBar.raise_()
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(change_pw_Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(change_pw_Dialog)

        self.UI_Changes(change_pw_Dialog)
        self.Handle_Buttons(change_pw_Dialog)

    def UI_Changes(self, change_pw_Dialog):
        self.tabWidget.tabBar().setVisible(False)
        change_pw_Dialog.setModal(True)
        self.progressBar.hide()
        self.label_6.setStyleSheet('QLabel {color: red;}')
        self.label_6.hide()
        self.label_10.setStyleSheet('QLabel {color: green;}')
        self.label_10.hide()
        self.pushButton_5.hide()


    def Handle_Buttons(self, change_pw_Dialog):
        self.pushButton.clicked.connect(self.executeUnlock)
        self.pushButton_2.clicked.connect(change_pw_Dialog.close)
        self.pushButton_4.clicked.connect(change_pw_Dialog.close)
        self.pushButton_5.clicked.connect(change_pw_Dialog.close)
        self.lineEdit_2.editingFinished.connect(self.showPasswordStrength)
        self.lineEdit_3.editingFinished.connect(self.showPasswordMatch)
        self.pushButton_3.clicked.connect(self.executeChangePassword)


    def moveToTab0(self):
        self.tabWidget.setCurrentIndex(0)

    def moveToTab1(self):
        self.tabWidget.setCurrentIndex(1)

    def executeUnlock(self):
        mp = re.sub("[^\w]", " ", self.plainTextEdit.toPlainText())
        sent_mp = mp.split()
        self.email = self.lineEdit.text().strip()
        if len(sent_mp) == 12 and Email().check_email(self.email):
            self.mp = mp[:-1]
            data = {'email': self.email, 'mp': self.mp}
            r = requests.post('https://127.0.0.1:5000/unlock', verify=False, json=data).json()
            if r['success']:
                self.moveToTab1()
            elif not r['success']:
                self.label_6.setText("Wrong Combination!")
                self.label_6.setStyleSheet('QLabel {color: red;}')
                self.label_6.show()
        elif not Email().check_email(self.email):
            self.label_6.setText("Wrong email form!")
            self.label_6.setStyleSheet('QLabel {color: red;}')
            self.label_6.show()
        else:
            self.label_6.setText("MP is not 12 words!")
            self.label_6.setStyleSheet('QLabel {color: red;}')
            self.label_6.show()

    def showPasswordStrength(self):
        pw = self.lineEdit_2.text()
        if len(pw) == 0:
            self.label_10.hide()
        elif len(pw) < 5:
            self.label_5.setText("Password too short!")
            self.label_5.setStyleSheet('QLabel {color: red;}')
            self.label_5.show()
        elif len(pw) > 32:
            self.label_5.setText("Password too long!")
            self.label_5.setStyleSheet('QLabel {color: red;}')
            self.label_5.show()
        else:
            stats = PasswordStats(pw).strength()
            if 0.8 < stats < 1:
                self.label_5.setText("Strength: Unbreakable!")
                self.label_5.setStyleSheet('QLabel {color: green;}')
                self.label_5.show()
            elif 0.6 < stats <= 0.8:
                self.label_5.setText("Strength: Very Good!")
                self.label_5.setStyleSheet('QLabel {color: dodgerblue;}')
                self.label_5.show()
            elif 0.4 < stats <= 0.6:
                self.label_5.setText("Strength: Good!")
                self.label_5.setStyleSheet('QLabel {color: goldenrod;}')
                self.label_5.show()
            else:
                self.label_5.setText("Strength: Weak!")
                self.label_5.setStyleSheet('QLabel {color: red;}')
                self.label_5.show()

    def showPasswordMatch(self):
        if self.lineEdit_2.text() == self.lineEdit_3.text():
            self.label_7.setText("Passwords match!")
            self.label_7.setStyleSheet('QLabel {color: green;}')
            self.label_7.show()
        else:
            self.label_7.setText("Passwords don't match!")
            self.label_7.setStyleSheet('QLabel {color: red;}')
            self.label_7.show()

    def getPasswordStrength(self):
        pw = self.lineEdit_2.text()
        if len(pw) == 0:
            return False
        elif len(pw) < 5:
            return False
        elif len(pw) > 32:
            return False
        else:
            stats = PasswordStats(pw).strength()
            if 0.8 < stats < 1:
                return True
            elif 0.6 < stats <= 0.8:
                return True
            elif 0.4 < stats <= 0.6:
                return True
            else:
                return True

    def getPasswordMatch(self):
        if self.lineEdit_2.text() == self.lineEdit_3.text():
            return True
        else:
            return False

    def executeChangePassword(self):
        if self.getPasswordStrength() and self.getPasswordMatch():
            data = {'email': self.email, 'pw': self.lineEdit_2.text(), 'mp': self.mp}
            r = requests.post('https://127.0.0.1:5000/changepw', verify=False, json=data).json()
            if r['success']:
                self.executeSuccess()



    def executeSuccess(self):
        self.label.hide()
        self.pushButton_3.hide()
        self.pushButton_4.hide()
        self.progressBar.show()
        v = 0
        while v <= 100:
            time.sleep(.005)
            self.progressBar.setProperty("value", v)
            v += 1
        self.progressBar.hide()
        self.label_10.show()
        self.pushButton_5.show()

    def retranslateUi(self, change_pw_Dialog):
        _translate = QtCore.QCoreApplication.translate
        change_pw_Dialog.setWindowTitle(_translate("change_pw_Dialog", "IronGate"))
        self.pushButton_2.setText(_translate("change_pw_Dialog", "Cancel"))
        self.pushButton.setText(_translate("change_pw_Dialog", "Unlock"))
        self.label_2.setText(_translate("change_pw_Dialog", "Mnemonic Phrase(MP):"))
        self.label.setText(_translate("change_pw_Dialog", "E-mail:"))
        self.label_6.setText(_translate("change_pw_Dialog", "Wrong Combination!"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("change_pw_Dialog", "Tab 1"))
        self.pushButton_3.setText(_translate("change_pw_Dialog", "Change Password"))
        self.label_3.setText(_translate("change_pw_Dialog", "New Password:"))
        self.pushButton_4.setText(_translate("change_pw_Dialog", "Cancel"))
        self.label_4.setText(_translate("change_pw_Dialog", "Repeat Password:"))
        self.label_10.setText(_translate("change_pw_Dialog", "Password Changed!"))
        self.pushButton_5.setText(_translate("change_pw_Dialog", "Exit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("change_pw_Dialog", "Tab 2"))
