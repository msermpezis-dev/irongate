# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\login_main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from encryption.decryptor import Decryptor
from encryption.generator import Generator
from encryption.keys import Keys

class Ui_Login_MainWindow(object):
    ar = []
    exit = 0
    MainWindow = None
    password = ''
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 320)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(400, 320))
        MainWindow.setMaximumSize(QtCore.QSize(400, 320))
        MainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\images/irongate-icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, -10, 411, 341))
        self.label_4.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(".\\images/light-background-small.png"))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(144, 270, 111, 31))
        self.pushButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 100, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 160, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 20, 401, 51))
        self.label_3.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(".\\images/irongate-logo.png"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 190, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setAutoDefault(True)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 190, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_3.setAutoDefault(True)
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.failed_login = QtWidgets.QLabel(self.centralwidget)
        self.failed_login.setEnabled(True)
        self.failed_login.setGeometry(QtCore.QRect(60, 230, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.failed_login.setFont(font)
        self.failed_login.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.failed_login.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.failed_login.setAlignment(QtCore.Qt.AlignCenter)
        self.failed_login.setObjectName("failed_login")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 80, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 140, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.MainWindow = MainWindow
        self.UI_Changes()
        self.Handle_Buttons()


    def Handle_Buttons(self):
        self.pushButton.clicked.connect(self.executeLogin)
        self.pushButton_2.clicked.connect(self.executeRegister)
        self.pushButton_3.clicked.connect(self.executeForgotPassword)

    def UI_Changes(self):
        self.failed_login.setStyleSheet('QLabel {color: red;}')
        self.failed_login.hide()
        self.pushButton_2.setStyleSheet('QPushButton {color: blue;}')
        self.pushButton_3.setStyleSheet('QPushButton {color: blue;}')
        
    def executeLogin(self):
        email = self.lineEdit.text().strip()
        pw = self.lineEdit_2.text()
        self.failed_login.hide()
        if len(email) == 0 or len(pw) == 0:
            self.failed_login.setText("Wrong Combination of E-mail/Password.")
            self.failed_login.show()
        else:
            data = {
                "email": email,
                "password": pw
            }

            try:
                r = requests.post('https://127.0.0.1:5000/login', verify=False, timeout=3, json=data)
                r.raise_for_status()
                r = r.json()
                if r['Status Code'] == 200:
                    gen = Generator()
                    k = Keys()
                    salt = gen.stringToBinary(r['salt_string'])
                    iv = gen.stringToBinary(r['iv_string'])
                    cipher = k.getCipher(pw, salt, iv)
                    enc_masterkey = gen.stringToBinary(r['enc_masterkey_string'])
                    masterkey = Decryptor().decrypt_mk(enc_masterkey, cipher)
                    readymasterkey = gen.stringToBinary(masterkey[:44])
                    mastercipher = k.getMasterCipher(readymasterkey, iv)
                    self.password = pw
                    self.ar.append(r['user_id'])
                    self.ar.append(email)
                    self.ar.append(mastercipher)
                    self.ar.append(salt)
                    self.ar.append(iv)

                    self.exit = 1
                    self.MainWindow.close()

                elif r['Status Code'] == -1:
                    self.failed_login.setText("Wrong Combination of E-mail/Password.")
                    self.failed_login.show()

                elif r['Status Code'] == -2:
                    self.failed_login.setText("Email doesn't exist.")
                    self.failed_login.show()
            except requests.exceptions.HTTPError as errh:
                self.failed_login.setText("Connection Error")
                self.failed_login.show()
                #print("Http Error:", errh)
            except requests.exceptions.ConnectionError as errc:
                self.failed_login.setText("Connection Error")
                self.failed_login.show()
                #print("Error Connecting:", errc)
            except requests.exceptions.Timeout as errt:
                self.failed_login.setText("Connection Error")
                self.failed_login.show()
                #print("Timeout Error:", errt)
            except requests.exceptions.RequestException as err:
                self.failed_login.setText("Connection Error")
                self.failed_login.show()
                #print("OOps: Something Else", err)






    def executeRegister(self):
        from register_dialog import Ui_register_dialog
        register_dialog = QtWidgets.QDialog(None, QtCore.Qt.WindowCloseButtonHint)
        ui = Ui_register_dialog()
        ui.setupUi(register_dialog)

        register_dialog.show()
        register_dialog.exec_()

    def executeForgotPassword(self):
        from change_pw_dialog import Ui_change_pw_Dialog
        change_pw = QtWidgets.QDialog(None, QtCore.Qt.WindowCloseButtonHint)
        ui = Ui_change_pw_Dialog()
        ui.setupUi(change_pw)
        change_pw.show()
        change_pw.exec_()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IronGate - Login"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.pushButton_2.setText(_translate("MainWindow", "Register"))
        self.pushButton_3.setText(_translate("MainWindow", "Forgot Password?"))
        self.failed_login.setText(_translate("MainWindow", "Wrong Combination of E-mail/Password."))
        self.label.setText(_translate("MainWindow", "E-mail:"))
        self.label_2.setText(_translate("MainWindow", "Password:"))

