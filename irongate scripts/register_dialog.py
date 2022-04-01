# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\register_dialog_new.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from pw_strength import PasswordStats
from email_plus import Email
import time
import re
import requests

class Ui_register_dialog(object):
    mnemonic = None
    mcvalue = None
    salt = None
    iv = None
    emailAvailable = False
    def setupUi(self, register_dialog):
        register_dialog.setObjectName("register_dialog")
        register_dialog.resize(400, 280)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(register_dialog.sizePolicy().hasHeightForWidth())
        register_dialog.setSizePolicy(sizePolicy)
        register_dialog.setMinimumSize(QtCore.QSize(400, 280))
        register_dialog.setMaximumSize(QtCore.QSize(400, 280))
        register_dialog.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\images/irongate-icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        register_dialog.setWindowIcon(icon)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget = QtWidgets.QTabWidget(register_dialog)
        self.tabWidget.setGeometry(QtCore.QRect(-2, -20, 421, 311))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(200, 240, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 240, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pw_match = QtWidgets.QLabel(self.tab)
        self.pw_match.setGeometry(QtCore.QRect(260, 160, 141, 31))
        self.pw_match.setObjectName("pw_match")
        self.pw_strength = QtWidgets.QLabel(self.tab)
        self.pw_strength.setGeometry(QtCore.QRect(260, 90, 141, 31))
        self.pw_strength.setObjectName("pw_strength")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(20, 50, 320, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFont(font)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 120, 320, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setFont(font)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 190, 320, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setFont(font)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(20, 160, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.email_exists = QtWidgets.QLabel(self.tab)
        self.email_exists.setGeometry(QtCore.QRect(260, 20, 141, 31))
        self.email_exists.setObjectName("email_exists")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(0, 10, 401, 291))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(".\\images/light-background-small.png"))
        self.label_7.setObjectName("label_7")
        self.label_7.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pw_match.raise_()
        self.pw_strength.raise_()
        self.lineEdit.raise_()
        self.label_2.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_2.raise_()
        self.label_3.raise_()
        self.label_6.raise_()
        self.email_exists.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.progressBar = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar.setGeometry(QtCore.QRect(160, 210, 131, 23))
        self.progressBar.setProperty("value", 10)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 240, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(10, 200, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(164, 240, 91, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(20, 80, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.mp_2 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.mp_2.setEnabled(True)
        self.mp_2.setGeometry(QtCore.QRect(10, 110, 371, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mp_2.setFont(font)
        self.mp_2.setReadOnly(False)
        self.mp_2.setPlainText("")
        self.mp_2.setOverwriteMode(False)
        self.mp_2.setObjectName("mp_2")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(0, 10, 401, 291))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(".\\images/light-background-small.png"))
        self.label_8.setObjectName("label_8")
        self.label_8.raise_()
        self.progressBar.raise_()
        self.label_4.raise_()
        self.pushButton_3.raise_()
        self.label.raise_()
        self.label_5.raise_()
        self.mp_2.raise_()
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(register_dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(register_dialog)

        self.UI_Changes(register_dialog)
        self.Handle_Buttons(register_dialog)

    def UI_Changes(self, register_dialog):
        self.tabWidget.tabBar().setVisible(False)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.email_exists.hide()
        self.pw_strength.hide()
        self.pw_match.hide()
        self.label.hide()
        self.progressBar.hide()
        self.pushButton_5.hide()
        register_dialog.setModal(True)

    def Handle_Buttons(self, register_dialog):
        self.lineEdit.editingFinished.connect(self.showEmailExistance)
        self.lineEdit_2.textChanged.connect(self.showPasswordStrength)
        self.lineEdit_3.textChanged.connect(self.showPasswordMatch)
        self.pushButton.clicked.connect(self.continueToMnemonicPhrase)
        self.pushButton_2.clicked.connect(register_dialog.close)
        self.pushButton_3.clicked.connect(self.getMnemonicPhraseMatch)
        self.pushButton_5.clicked.connect(register_dialog.close)

    def moveToTab0(self):
        self.tabWidget.setCurrentIndex(0)

    def moveToTab1(self):
        self.tabWidget.setCurrentIndex(1)

    def getEmailExistance(self, email):
        return requests.post('https://127.0.0.1:5000/checkmail', verify=False, json={'email': email}).json()['isEmail']

    def showEmailExistance(self):
        email = self.lineEdit.text().strip()
        if Email().check_email(email) and 0 < len(email) < 51:
            if not self.getEmailExistance(email):
                self.email_exists.setText("E-mail Available!")
                self.email_exists.setStyleSheet('QLabel {color: green;}')
                self.email_exists.show()
                self.emailAvailable = True
                return True
            else:
                self.email_exists.setText("E-mail Exists!")
                self.email_exists.setStyleSheet('QLabel {color: red;}')
                self.email_exists.show()
                self.emailAvailable = False
                return False
        elif len(email) > 50:
            self.email_exists.setText("E-mail too long!")
            self.email_exists.setStyleSheet('QLabel {color: red;}')
            self.email_exists.show()
            return False
        else:
            self.email_exists.setText("Not E-Mail!")
            self.email_exists.setStyleSheet('QLabel {color: red;}')
            self.email_exists.show()
            return False

    def showPasswordStrength(self):
        pw = self.lineEdit_2.text()
        if len(pw) == 0:
            self.pw_strength.hide()
        elif len(pw) < 5:
            self.pw_strength.setText("Password too short!")
            self.pw_strength.setStyleSheet('QLabel {color: red;}')
            self.pw_strength.show()
        elif len(pw) > 32:
            self.pw_strength.setText("Password too long!")
            self.pw_strength.setStyleSheet('QLabel {color: red;}')
            self.pw_strength.show()
        else:
            stats = PasswordStats(pw).strength()
            if 0.8 < stats < 1:
                self.pw_strength.setText("Strength: Unbreakable!")
                self.pw_strength.setStyleSheet('QLabel {color: green;}')
                self.pw_strength.show()
            elif 0.6 < stats <= 0.8:
                self.pw_strength.setText("Strength: Very Good!")
                self.pw_strength.setStyleSheet('QLabel {color: dodgerblue;}')
                self.pw_strength.show()
            elif 0.4 < stats <= 0.6:
                self.pw_strength.setText("Strength: Good!")
                self.pw_strength.setStyleSheet('QLabel {color: goldenrod;}')
                self.pw_strength.show()
            else:
                self.pw_strength.setText("Strength: Weak!")
                self.pw_strength.setStyleSheet('QLabel {color: red;}')
                self.pw_strength.show()

    def showPasswordMatch(self):
        if self.lineEdit_2.text() == self.lineEdit_3.text():
            self.pw_match.setText("Passwords match!")
            self.pw_match.setStyleSheet('QLabel {color: green;}')
            self.pw_match.show()
        else:
            self.pw_match.setText("Passwords don't match!")
            self.pw_match.setStyleSheet('QLabel {color: red;}')
            self.pw_match.show()


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

    def continueToMnemonicPhrase(self):
        if self.emailAvailable and self.getPasswordStrength() and self.getPasswordMatch():
            self.mp_2.setPlainText("")
            self.moveToTab1()
            data = {'email': self.lineEdit.text().strip()}
            r = requests.post('https://127.0.0.1:5000/sendmail', verify=False, json=data).json()
            self.mcvalue = r['mcvalue']
            self.salt = r['salt']
            self.iv = r['iv']


    def getMnemonicPhraseMatch(self):
        mp = re.sub("[^\w]", " ", self.mp_2.toPlainText())
        sent_mp = mp.split()
        if len(sent_mp) == 12:
            self.mnemonic = mp[:-1]
            data = {'email': self.lineEdit.text(), 'salt': self.salt, 'iv': self.iv,
                    'mcvalue': self.mcvalue, 'mp': self.mnemonic, 'password': self.lineEdit_3.text()
                    }
            r = requests.post('https://127.0.0.1:5000/register', verify=False, json=data).json()

            if r['Status Code'] == 200:
                self.executeSuccess()
            else:
                self.label.setStyleSheet('QLabel {color: red;}')
                self.label.setText("Incorrect Mnemonic Phrase")
                self.label.show()
        else:
            self.label.setStyleSheet('QLabel {color: red;}')
            self.label.setText("Incorrect Mnemonic Phrase")
            self.label.show()


    def executeSuccess(self):
        self.label.hide()
        self.label.setStyleSheet('QLabel {color: green;}')
        self.label.setText("Registration Complete!")
        self.pushButton_3.hide()
        self.progressBar.show()
        v = 0
        while v <= 100:
            time.sleep(.005)
            self.progressBar.setProperty("value", v)
            v += 1
        self.progressBar.hide()
        self.label.show()
        self.pushButton_5.raise_()
        self.pushButton_5.show()


    def retranslateUi(self, register_dialog):
        _translate = QtCore.QCoreApplication.translate
        register_dialog.setWindowTitle(_translate("register_dialog", "IronGate - Registration"))
        self.pushButton.setText(_translate("register_dialog", "Continue"))
        self.pushButton_2.setText(_translate("register_dialog", "Cancel"))
        self.pw_match.setText(_translate("register_dialog", "passwords match"))
        self.pw_strength.setText(_translate("register_dialog", "password strenfgth"))
        self.label_2.setText(_translate("register_dialog", "Password:"))
        self.label_3.setText(_translate("register_dialog", "E-mail:"))
        self.label_6.setText(_translate("register_dialog", "Retype Password:"))
        self.email_exists.setText(_translate("register_dialog", "email exists"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("register_dialog", "Tab 1"))
        self.label_4.setText(_translate("register_dialog", "Mnemonic Phrase was sent to your e-mail."))
        self.pushButton_3.setText(_translate("register_dialog", "Complete"))
        self.label.setText(_translate("register_dialog", "Registration Complete!"))
        self.pushButton_5.setText(_translate("register_dialog", "Close"))
        self.label_5.setText(_translate("register_dialog", "Type Mnemonic Phrase:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("register_dialog", "Tab 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    register_dialog = QtWidgets.QDialog()
    ui = Ui_register_dialog()
    ui.setupUi(register_dialog)
    register_dialog.show()
    sys.exit(app.exec_())
