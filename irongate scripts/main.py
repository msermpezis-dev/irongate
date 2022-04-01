# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import sys
import base64
from PyQt5 import QtCore, QtGui, QtWidgets
from add_dialog import Ui_Dialog_Add
from remove_all_dialog import Ui_Dialog_DelAll
from remove_selected_dialog import Ui_Dialog_Del
from login_main import Ui_Login_MainWindow
from encryption.decryptor import Decryptor
from encryption.generator import Generator
from pw_strength import PasswordStats
import requests
import re


class Ui_MainWindow(object):
    values = [] #[0]:user_id, [1]:email, [2]:mastercipher, [3]: salt, [4]: iv
    password = ''
    mp = ''
    entities = [] #[0]:entity_id, [1]:entity_name, [2]:entity_un, [3]:entity_pw, [4]:note
    in_search = False
    pw_show = False

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 720))
        MainWindow.setMaximumSize(QtCore.QSize(800, 720))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\images/irongate-icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, -10, 1280, 720))
        self.background.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.background.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(".\\images/background.jpg"))
        self.background.setObjectName("background")

        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(0, 0, 200, 80))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(".\\images/irongate-logo.png"))
        self.logo.setObjectName("logo")
        self.user_icon = QtWidgets.QLabel(self.centralwidget)
        self.user_icon.setGeometry(QtCore.QRect(690, 10, 80, 80))
        self.user_icon.setText("")
        self.user_icon.setPixmap(QtGui.QPixmap(".\\images/user-icon.png"))
        self.user_icon.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.user_icon.setObjectName("user_icon")
        self.welcome = QtWidgets.QLabel(self.centralwidget)
        self.welcome.setGeometry(QtCore.QRect(10, 70, 180, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.welcome.setFont(font)
        self.welcome.setObjectName("welcome")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(10, 100, 781, 591))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.tabWidget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.search = QtWidgets.QPushButton(self.tab_1)
        self.search.setGeometry(QtCore.QRect(691, 9, 33, 33))
        self.search.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\images/search-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search.setIcon(icon1)
        self.search.setIconSize(QtCore.QSize(27, 27))
        self.search.setObjectName("search")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_1)
        self.lineEdit.setGeometry(QtCore.QRect(420, 10, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("Search Name...")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_1)
        self.tableWidget.setGeometry(QtCore.QRect(0, 50, 775, 535))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setColumnHidden(4, True)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.setColumnWidth(0, 120)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.setColumnWidth(1, 120)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.setColumnWidth(2, 120)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(0, 0, 0))
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.setColumnWidth(3, 398)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.addButton = QtWidgets.QPushButton(self.tab_1)
        self.addButton.setGeometry(QtCore.QRect(4, 4, 41, 41))
        self.addButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\images/add-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addButton.setIcon(icon2)
        self.addButton.setIconSize(QtCore.QSize(30, 30))
        self.addButton.setObjectName("addButton")
        self.comboBox = QtWidgets.QComboBox(self.tab_1)
        self.comboBox.setGeometry(QtCore.QRect(56, 5, 101, 39))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.settings = QtWidgets.QPushButton(self.tab_1)
        self.settings.setGeometry(QtCore.QRect(730, 4, 41, 41))
        self.settings.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\\images/settings-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings.setIcon(icon3)
        self.settings.setIconSize(QtCore.QSize(38, 38))
        self.settings.setObjectName("settings")
        self.remove = QtWidgets.QPushButton(self.tab_1)
        self.remove.setGeometry(QtCore.QRect(156, 4, 41, 41))
        self.remove.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(".\\images/remove-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remove.setIcon(icon4)
        self.remove.setIconSize(QtCore.QSize(35, 35))
        self.remove.setObjectName("remove")
        self.show_pw = QtWidgets.QPushButton(self.tab_1)
        self.show_pw.setGeometry(QtCore.QRect(206, 4, 41, 41))
        self.show_pw.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(".\\images/pw_on.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.show_pw.setIcon(icon5)
        self.show_pw.setIconSize(QtCore.QSize(40, 40))
        self.show_pw.setObjectName("show_pw")
        self.refresh_button = QtWidgets.QPushButton(self.tab_1)
        self.refresh_button.setGeometry(QtCore.QRect(256, 4, 41, 41))
        self.refresh_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(".\\images/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refresh_button.setIcon(icon5)
        self.refresh_button.setIconSize(QtCore.QSize(35, 35))
        self.refresh_button.setObjectName("refresh_button")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()

        self.tab_2.setObjectName("tab_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 50, 421, 171))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 20, 131, 31))
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 50, 381, 51))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(30, 120, 241, 21))
        self.label_5.setObjectName("label_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 120, 75, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setDefault(True)
        self.pushButton_3.setAutoDefault(True)

        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setEnabled(False)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 250, 551, 181))
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 101, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 111, 31))
        self.label_4.setObjectName("label_4")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_9.setGeometry(QtCore.QRect(120, 30, 271, 31))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_9.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_10.setGeometry(QtCore.QRect(120, 80, 271, 31))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_10.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(130, 130, 151, 21))
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(410, 30, 181, 31))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(410, 80, 181, 31))
        self.label_10.setObjectName("label_10")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_4.setGeometry(QtCore.QRect(274, 130, 111, 31))
        self.pushButton_4.setObjectName("pushButton_4")

        self.back = QtWidgets.QPushButton(self.tab_2)
        self.back.setGeometry(QtCore.QRect(0, 0, 70, 40))
        self.back.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(".\\images/back-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back.setIcon(icon8)
        self.back.setIconSize(QtCore.QSize(65, 35))
        self.back.setObjectName("back")
        self.tabWidget.addTab(self.tab_2, "")
        self.logo.raise_()
        self.user_icon.raise_()
        self.welcome.raise_()
        self.tabWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Handle_Buttons()
        self.UI_Changes()
        self.executeLogin()


    def Handle_Buttons(self):
        self.addButton.clicked.connect(self.executeAddDialog)
        self.settings.clicked.connect(self.moveToTab1)
        self.back.clicked.connect(self.moveToTab0)
        self.remove.clicked.connect(self.chooseDel)
        self.show_pw.clicked.connect(self.executeShowPassword)
        self.refresh_button.clicked.connect(self.executeRefresh)
        self.search.clicked.connect(self.executeSearch)
        self.pushButton_3.clicked.connect(self.executeUnlock)
        self.pushButton_4.clicked.connect(self.executeChangePassword)
        self.lineEdit.textChanged.connect(self.executeSearchRefresh)
        self.lineEdit_9.editingFinished.connect(self.showPasswordStrenth)
        self.lineEdit_10.editingFinished.connect(self.showPasswordMatch)



    def UI_Changes(self):
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.tabBar().setVisible(False)
        self.label_5.hide()
        self.label_6.hide()
        self.label_6.setStyleSheet('QLabel {color: green;}')


    def moveToTab0(self):
        self.tabWidget.setCurrentIndex(0)
        self.groupBox_3.setEnabled(False)
        self.groupBox_2.setEnabled(True)
        self.plainTextEdit.setPlainText("")
        self.label_5.hide()
        self.lineEdit_9.setText("")
        self.lineEdit_10.setText("")
        self.label_6.hide()

    def moveToTab1(self):
        self.tabWidget.setCurrentIndex(1)

    def executeLogin(self):
        login_dialog = QtWidgets.QDialog(None, QtCore.Qt.WindowCloseButtonHint)
        ui = Ui_Login_MainWindow()
        ui.setupUi(login_dialog)
        login_dialog.show()
        login_dialog.exec_()
        self.values = ui.ar
        self.password = ui.password
        if ui.exit == 0:
            sys.exit()
        self.welcome.setText(self.values[1])
        self.setupEntries()

    def setupEntries(self):
        mastercipher = self.values[2]
        data = {
            "user_id": self.values[0],
            'pw': self.password
        }

        r = requests.post('https://127.0.0.1:5000/entities', verify=False, json=data).json()
        self.entities = []
        if len(r) > 0 and len(r[0]) == 5:
            length = len(r)
            self.tableWidget.setRowCount(length)
            dec = Decryptor()
            for i in range(length):
                self.entities.append([r[i]['id'], r[i]['en'], r[i]['eun'], r[i]['epw'], r[i]['enotes'], str(i)])
                ready_eun = Generator().stringToBinary(self.entities[i][2])
                dun = dec.decrypt(ready_eun, mastercipher).decode('utf-8')
                self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(self.entities[i][1]))
                self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(dun))
                self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem("••••••••••"))
                self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(self.entities[i][4]))
                self.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(self.entities[i][5]))
        else:
            self.tableWidget.setRowCount(0)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(".\\images/pw_on.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.show_pw.setIcon(icon6)
        self.show_pw.setIconSize(QtCore.QSize(37, 37))
        self.pw_show = False
        self.in_search = False


    def executeAddDialog(self):
        Dialog = QtWidgets.QDialog(None, QtCore.Qt.WindowCloseButtonHint)
        ui = Ui_Dialog_Add()
        ui.user_id = self.values[0]
        ui.pw = self.password
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()
        self.setupEntries()

    def chooseDel(self):
        if self.comboBox.currentIndex() == 0:
            self.executeDelDialog()
        else:
            self.executeDelAllDialog()

    def executeDelAllDialog(self):
        Dialog = QtWidgets.QDialog(None, QtCore.Qt.WindowCloseButtonHint)
        ui = Ui_Dialog_DelAll()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()
        if ui.exit == 1:
            data = {'user_id': self.values[0], 'pw': self.password, "e_id": []}
            if self.in_search:
                all = self.tableWidget.rowCount()
                for i in range(all):
                    e_id = int(self.tableWidget.item(i, 4).text())
                    data["e_id"].append(self.entities[e_id][0])
                
            else:
                for i in self.entities:
                    data["e_id"].append(i[0])
            requests.post('https://127.0.0.1:5000/remove', verify=False, json=data)
            self.executeRefresh()

    def executeDelDialog(self):
        Dialog = QtWidgets.QDialog(None, QtCore.Qt.WindowCloseButtonHint)
        ui = Ui_Dialog_Del()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()
        if ui.exit == 1:
            selected = self.tableWidget.selectedItems()
            data = {'user_id': self.values[0], 'pw': self.password, "e_id": []}
            for i in selected:
                e_id = int(self.tableWidget.item(i.row(), 4).text())
                data["e_id"].append(self.entities[e_id][0])
            if len(data["e_id"]) > 0:
                requests.post('https://127.0.0.1:5000/remove', verify=False, json=data)
                self.executeRefresh()


    def executeShowPassword(self):
        if self.pw_show:
            for i in range(len(self.entities)):
                self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem("••••••••••"))
                icon6 = QtGui.QIcon()
                icon6.addPixmap(QtGui.QPixmap(".\\images/pw_on.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.show_pw.setIcon(icon6)
                self.show_pw.setIconSize(QtCore.QSize(37, 37))
                self.pw_show = False
        else:
            for i in range(len(self.entities)):
                mastercipher = self.values[2]
                d = Decryptor().decrypt(Generator().stringToBinary(self.entities[i][3]), mastercipher).decode()
                self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(d))
                icon7 = QtGui.QIcon()
                icon7.addPixmap(QtGui.QPixmap(".\\images/pw_off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.show_pw.setIcon(icon7)
                self.show_pw.setIconSize(QtCore.QSize(37, 37))
                self.pw_show = True

    def executeRefresh(self):
        if self.in_search:
            self.lineEdit.setText('')
            self.setupEntries()
            self.in_search = False
        else:
            self.setupEntries()
            self.in_search = False

    def executeSearchRefresh(self):
        if len(self.lineEdit.text()) == 0 and self.in_search:
            self.setupEntries()
            self.in_search = False


    def executeSearch(self):
        # 0:entity_id, 1:entity_name, 2:entity_un, 3:entity_pw, 4:note
        if len(self.lineEdit.text()) > 0:
            icon6 = QtGui.QIcon()
            icon6.addPixmap(QtGui.QPixmap(".\\images/pw_on.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.show_pw.setIcon(icon6)
            self.show_pw.setIconSize(QtCore.QSize(37, 37))
            self.pw_show = False
            data = self.entities
            elem = self.lineEdit.text()
            ids = []
            n = 0
            for row in data:
                if elem in row[1]:
                    ids.append(n)
                n += 1
            self.setupFoundEntries(ids)
            self.in_search = True



    def setupFoundEntries(self, ids):
        length = len(ids)
        if length > 0:
            self.tableWidget.setRowCount(0)
            self.tableWidget.setRowCount(length)
            i = 0
            dec = Decryptor()
            for id in ids:
                mastercipher = self.values[2]
                ready_eun = Generator().stringToBinary(self.entities[i][2])
                dun = dec.decrypt(ready_eun, mastercipher).decode('utf-8')
                self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(self.entities[id][1]))
                self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(dun))
                self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem("••••••••••"))
                self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(self.entities[id][4]))
                self.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(self.entities[id][5]))
                i += 1
        else:
            self.tableWidget.setRowCount(0)

    def executeUnlock(self):
        mp = re.sub("[^\w]", " ", self.plainTextEdit.toPlainText()).split()
        if len(mp) == 12:
            re_mp = ""
            for word in mp:
                re_mp += word + " "
            mp = re_mp[:-1]
            data = {'email': self.values[1], 'mp': mp}
            r = requests.post('https://127.0.0.1:5000/unlock', verify=False, json=data).json()
            if r['success']:
                self.mp = mp
                self.groupBox_3.setEnabled(True)
                self.groupBox_2.setEnabled(False)

            elif not r['success']:
                self.label_5.setText("Wrong Combination!")
                self.label_5.setStyleSheet('QLabel {color: red;}')
                self.label_5.show()
        else:
            self.label_5.setText("MP is not 12 words!")
            self.label_5.setStyleSheet('QLabel {color: red;}')
            self.label_5.show()

    def showPasswordStrenth(self):
        pw = self.lineEdit_9.text()
        if len(pw) == 0:
            self.label_9.hide()
            return False
        elif len(pw) < 5:
            self.label_9.setText("Password too short!")
            self.label_9.setStyleSheet('QLabel {color: red;}')
            self.label_9.show()
            return False
        elif len(pw) > 32:
            self.label_9.setText("Password too long!")
            self.label_9.setStyleSheet('QLabel {color: red;}')
            self.label_9.show()
            return False
        else:
            stats = PasswordStats(pw).strength()
            if 0.8 < stats < 1:
                self.label_9.setText("Strength: Unbreakable!")
                self.label_9.setStyleSheet('QLabel {color: green;}')
                self.label_9.show()
                return True
            elif 0.6 < stats <= 0.8:
                self.label_9.setText("Strength: Very Good!")
                self.label_9.setStyleSheet('QLabel {color: dodgerblue;}')
                self.label_9.show()
                return True
            elif 0.4 < stats <= 0.6:
                self.label_9.setText("Strength: Good!")
                self.label_9.setStyleSheet('QLabel {color: goldenrod;}')
                self.label_9.show()
                return True
            else:
                self.label_9.setText("Strength: Weak!")
                self.label_9.setStyleSheet('QLabel {color: red;}')
                self.label_9.show()
                return True

    def showPasswordMatch(self):
        pw1 = self.lineEdit_9.text()
        pw2 = self.lineEdit_10.text()
        if pw1 == pw2 and not len(pw2) == 0:
            self.label_10.setText("Passwords match!")
            self.label_10.setStyleSheet('QLabel {color: green;}')
            self.label_10.show()
            return True
        else:
            self.label_10.setText("Passwords don't match!")
            self.label_10.setStyleSheet('QLabel {color: red;}')
            self.label_10.show()
            return False

    def executeChangePassword(self):
        if self.showPasswordMatch() and self.showPasswordStrenth():
            data = {'email': self.values[1], 'pw': self.lineEdit_10.text(), 'mp': self.mp}
            r = requests.post('https://127.0.0.1:5000/changepw', verify=False, json=data).json()
            if r['success']:
                self.label_9.hide()
                self.label_10.hide()
                self.label_6.show()
                self.groupBox_3.setEnabled(False)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IronGate"))
        self.welcome.setText(_translate("MainWindow", "Welcome <user>!"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Username"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Password"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Notes"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Delete Selected"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Delete All"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Entries"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Unlock Change Password"))
        self.pushButton_3.setText(_translate("MainWindow", "Unlock"))
        self.label.setText(_translate("MainWindow", "Mnemonic Phrase:"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Change Password"))
        self.label_3.setText(_translate("MainWindow", "New Password:"))
        self.label_4.setText(_translate("MainWindow", "Repeat Password:"))
        self.label_5.setText(_translate("MainWindow", "Change Password Unlocked!"))
        self.label_6.setText(_translate("MainWindow", "Password Changed!"))
        self.pushButton_4.setText(_translate("MainWindow", "Change Password"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "User Settings"))

