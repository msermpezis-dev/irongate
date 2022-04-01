# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\remove_all_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_DelAll(object):
    exit = 0
    dialog = None
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 120)
        Dialog.setModal(True)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(400, 120))
        Dialog.setMaximumSize(QtCore.QSize(400, 120))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\images/irongate-icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, -20, 381, 101))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(90, 70, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 70, 81, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setDefault(True)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.dialog = Dialog
        self.Handle_Buttons(Dialog)

    def Handle_Buttons(self, Dialog):
        self.pushButton_2.clicked.connect(Dialog.close)
        self.pushButton.clicked.connect(self.executeYes)

    def executeYes(self):
        self.exit = 1
        self.dialog.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "IronGate"))
        self.label.setText(_translate("Dialog", "Are you sure you want to remove all entries?"))
        self.pushButton.setText(_translate("Dialog", "Yes"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))


