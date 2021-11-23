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
        MainWindow.resize(890, 601)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.enviarInicio_pushButton = QPushButton(self.tab)
        self.enviarInicio_pushButton.setObjectName(u"enviarInicio_pushButton")

        self.gridLayout_2.addWidget(self.enviarInicio_pushButton, 1, 0, 1, 1)

        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 3, 3, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.green_spinBox = QSpinBox(self.groupBox)
        self.green_spinBox.setObjectName(u"green_spinBox")
        self.green_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.green_spinBox, 2, 4, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.red_spinBox = QSpinBox(self.groupBox)
        self.red_spinBox.setObjectName(u"red_spinBox")
        self.red_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.red_spinBox, 1, 4, 1, 1)

        self.line_3 = QFrame(self.groupBox)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_3, 2, 2, 1, 1)

        self.line_5 = QFrame(self.groupBox)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_5, 4, 2, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 2, 3, 1, 1)

        self.origenY_spinBox = QSpinBox(self.groupBox)
        self.origenY_spinBox.setObjectName(u"origenY_spinBox")
        self.origenY_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.origenY_spinBox, 2, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 1, 3, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.line_6 = QFrame(self.groupBox)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_6, 5, 2, 1, 1)

        self.blue_spinBox = QSpinBox(self.groupBox)
        self.blue_spinBox.setObjectName(u"blue_spinBox")
        self.blue_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.blue_spinBox, 3, 4, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 0, 3, 1, 1)

        self.origenX_spinBox = QSpinBox(self.groupBox)
        self.origenX_spinBox.setObjectName(u"origenX_spinBox")
        self.origenX_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.origenX_spinBox, 1, 1, 1, 1)

        self.id_spinBox = QSpinBox(self.groupBox)
        self.id_spinBox.setObjectName(u"id_spinBox")
        self.id_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.id_spinBox, 0, 1, 1, 1)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 0, 2, 1, 1)

        self.line_4 = QFrame(self.groupBox)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_4, 3, 2, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.velocidad_spinBox = QSpinBox(self.groupBox)
        self.velocidad_spinBox.setObjectName(u"velocidad_spinBox")
        self.velocidad_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.velocidad_spinBox, 5, 1, 1, 1)

        self.destinoX_spinBox = QSpinBox(self.groupBox)
        self.destinoX_spinBox.setObjectName(u"destinoX_spinBox")
        self.destinoX_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.destinoX_spinBox, 3, 1, 1, 1)

        self.line_2 = QFrame(self.groupBox)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 1, 2, 1, 1)

        self.destinoY_spinBox = QSpinBox(self.groupBox)
        self.destinoY_spinBox.setObjectName(u"destinoY_spinBox")
        self.destinoY_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.destinoY_spinBox, 4, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.mostrar_pushButton = QPushButton(self.tab)
        self.mostrar_pushButton.setObjectName(u"mostrar_pushButton")

        self.gridLayout_2.addWidget(self.mostrar_pushButton, 3, 0, 1, 1)

        self.salida_plainTextEdit = QPlainTextEdit(self.tab)
        self.salida_plainTextEdit.setObjectName(u"salida_plainTextEdit")

        self.gridLayout_2.addWidget(self.salida_plainTextEdit, 0, 1, 4, 1)

        self.enviarFinal_pushButton = QPushButton(self.tab)
        self.enviarFinal_pushButton.setObjectName(u"enviarFinal_pushButton")

        self.gridLayout_2.addWidget(self.enviarFinal_pushButton, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.mostrarTabla_pushButton = QPushButton(self.tab_2)
        self.mostrarTabla_pushButton.setObjectName(u"mostrarTabla_pushButton")

        self.gridLayout_4.addWidget(self.mostrarTabla_pushButton, 1, 4, 1, 1)

        self.table = QTableWidget(self.tab_2)
        self.table.setObjectName(u"table")

        self.gridLayout_4.addWidget(self.table, 0, 0, 1, 5)

        self.buscar_pushButton = QPushButton(self.tab_2)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")

        self.gridLayout_4.addWidget(self.buscar_pushButton, 1, 3, 1, 1)

        self.buscar_lineEdit = QLineEdit(self.tab_2)
        self.buscar_lineEdit.setObjectName(u"buscar_lineEdit")

        self.gridLayout_4.addWidget(self.buscar_lineEdit, 1, 0, 1, 1)

        self.orderById_pushButton = QPushButton(self.tab_2)
        self.orderById_pushButton.setObjectName(u"orderById_pushButton")

        self.gridLayout_4.addWidget(self.orderById_pushButton, 1, 1, 1, 1)

        self.orderBySpeed_pushButton = QPushButton(self.tab_2)
        self.orderBySpeed_pushButton.setObjectName(u"orderBySpeed_pushButton")

        self.gridLayout_4.addWidget(self.orderBySpeed_pushButton, 1, 2, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_3 = QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.graphicsView = QGraphicsView(self.tab_3)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_3.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.dibujar = QPushButton(self.tab_3)
        self.dibujar.setObjectName(u"dibujar")

        self.gridLayout_3.addWidget(self.dibujar, 1, 0, 1, 1)

        self.limpiar = QPushButton(self.tab_3)
        self.limpiar.setObjectName(u"limpiar")

        self.gridLayout_3.addWidget(self.limpiar, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_6 = QGridLayout(self.tab_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.grafo_graphicsView = QGraphicsView(self.tab_4)
        self.grafo_graphicsView.setObjectName(u"grafo_graphicsView")

        self.gridLayout_6.addWidget(self.grafo_graphicsView, 0, 0, 7, 1)

        self.grafo_plainTextEdit = QPlainTextEdit(self.tab_4)
        self.grafo_plainTextEdit.setObjectName(u"grafo_plainTextEdit")

        self.gridLayout_6.addWidget(self.grafo_plainTextEdit, 0, 1, 1, 2)

        self.label_11 = QLabel(self.tab_4)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_6.addWidget(self.label_11, 1, 1, 1, 1)

        self.grafo_origenx_spinBox = QSpinBox(self.tab_4)
        self.grafo_origenx_spinBox.setObjectName(u"grafo_origenx_spinBox")

        self.gridLayout_6.addWidget(self.grafo_origenx_spinBox, 1, 2, 1, 1)

        self.label_12 = QLabel(self.tab_4)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_6.addWidget(self.label_12, 2, 1, 1, 1)

        self.grafo_origeny_spinBox = QSpinBox(self.tab_4)
        self.grafo_origeny_spinBox.setObjectName(u"grafo_origeny_spinBox")

        self.gridLayout_6.addWidget(self.grafo_origeny_spinBox, 2, 2, 1, 1)

        self.grafo_recorrer_pushButton = QPushButton(self.tab_4)
        self.grafo_recorrer_pushButton.setObjectName(u"grafo_recorrer_pushButton")

        self.gridLayout_6.addWidget(self.grafo_recorrer_pushButton, 3, 1, 1, 2)

        self.grafo_mostrar_pushButton = QPushButton(self.tab_4)
        self.grafo_mostrar_pushButton.setObjectName(u"grafo_mostrar_pushButton")

        self.gridLayout_6.addWidget(self.grafo_mostrar_pushButton, 4, 1, 1, 2)

        self.grafo_dibujar_pushButton = QPushButton(self.tab_4)
        self.grafo_dibujar_pushButton.setObjectName(u"grafo_dibujar_pushButton")

        self.gridLayout_6.addWidget(self.grafo_dibujar_pushButton, 5, 1, 1, 2)

        self.grafo_profundidad_pushButton = QPushButton(self.tab_4)
        self.grafo_profundidad_pushButton.setObjectName(u"grafo_profundidad_pushButton")

        self.gridLayout_6.addWidget(self.grafo_profundidad_pushButton, 6, 1, 1, 2)

        self.tabWidget.addTab(self.tab_4, "")

        self.gridLayout_5.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 890, 22))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir...", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar...", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.enviarInicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al inicio", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Capturar particulas", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"velocidad", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"blue", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"destino x", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"origen en y", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"green", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"origen en x", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"red", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"destino y", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"color :", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"id", None))
        self.mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"mostrar", None))
        self.enviarFinal_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al final", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.mostrarTabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.buscar_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar por ID", None))
        self.orderById_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar ID", None))
        self.orderBySpeed_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar velocidad", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.dibujar.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.limpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Graficos", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Origen X", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Origen Y", None))
        self.grafo_recorrer_pushButton.setText(QCoreApplication.translate("MainWindow", u"Recorrer", None))
        self.grafo_mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.grafo_dibujar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.grafo_profundidad_pushButton.setText(QCoreApplication.translate("MainWindow", u"Recorrido profundidad", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Grafo", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

