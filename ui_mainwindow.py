# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(562, 337)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 2, 0, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 1, 3, 1, 1)

        self.spinBox_10 = QSpinBox(self.groupBox)
        self.spinBox_10.setObjectName(u"spinBox_10")
        self.spinBox_10.setMaximum(255)

        self.gridLayout.addWidget(self.spinBox_10, 3, 4, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 2, 3, 1, 1)

        self.spinBox = QSpinBox(self.groupBox)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.spinBox_4 = QSpinBox(self.groupBox)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_4, 3, 1, 1, 1)

        self.spinBox_5 = QSpinBox(self.groupBox)
        self.spinBox_5.setObjectName(u"spinBox_5")
        self.spinBox_5.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_5, 4, 1, 1, 1)

        self.spinBox_9 = QSpinBox(self.groupBox)
        self.spinBox_9.setObjectName(u"spinBox_9")
        self.spinBox_9.setMaximum(255)

        self.gridLayout.addWidget(self.spinBox_9, 2, 4, 1, 1)

        self.spinBox_2 = QSpinBox(self.groupBox)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_2, 1, 1, 1, 1)

        self.spinBox_8 = QSpinBox(self.groupBox)
        self.spinBox_8.setObjectName(u"spinBox_8")
        self.spinBox_8.setMaximum(255)

        self.gridLayout.addWidget(self.spinBox_8, 1, 4, 1, 1)

        self.spinBox_3 = QSpinBox(self.groupBox)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_3, 2, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 0, 3, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 3, 3, 1, 1)

        self.spinBox_6 = QSpinBox(self.groupBox)
        self.spinBox_6.setObjectName(u"spinBox_6")
        self.spinBox_6.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_6, 5, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 0, 2, 1, 1)

        self.line_2 = QFrame(self.groupBox)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 1, 2, 1, 1)

        self.line_3 = QFrame(self.groupBox)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_3, 2, 2, 1, 1)

        self.line_4 = QFrame(self.groupBox)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_4, 3, 2, 1, 1)

        self.line_5 = QFrame(self.groupBox)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_5, 4, 2, 1, 1)

        self.line_6 = QFrame(self.groupBox)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_6, 5, 2, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 562, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Capturar particulas", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"red", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"destino x", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"green", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"origen en x", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"id", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"color :", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"origen en y", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"destino y", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"blue", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"velocidad", None))
    # retranslateUi

