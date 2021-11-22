from os import pardir
from PySide2.QtGui import QColor, QPen
from PySide2.QtWidgets import QFileDialog, QGraphicsScene, QMainWindow, QMessageBox, QTableWidgetItem
from models.algoritmos import distancia_euclidiana
from .ui_mainwindow import Ui_MainWindow
from models.particula import Particula
from models.startLabs import StartLabs # administradora
from pprint import pprint #imprimir dicionarios
from collections import deque, defaultdict


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.acelerador = StartLabs()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Botones
        self.ui.enviarInicio_pushButton.clicked.connect(self.clickEnviarInicio)
        self.ui.enviarFinal_pushButton.clicked.connect(self.clickEnviarFinal)
        self.ui.mostrar_pushButton.clicked.connect(self.mostrar)

        # Qaction
        self.ui.actionAbrir.triggered.connect( self.abrir )
        self.ui.actionGuardar.triggered.connect( self.guardar )

        # Table
        self.ui.buscar_pushButton.clicked.connect( self.buscar )
        self.ui.mostrarTabla_pushButton.clicked.connect( self.mostrarTabla )
        self.ui.orderById_pushButton.clicked.connect( self.ordenarId )
        self.ui.orderBySpeed_pushButton.clicked.connect( self.ordenarVelocidad )


        # Graficos
        self.ui.limpiar.clicked.connect( self.limpiar )
        self.ui.dibujar.clicked.connect( self.dibujar )
        self.scene = QGraphicsScene()
        self.scene2 = QGraphicsScene()
        self.ui.graphicsView.setScene( self.scene )
        self.ui.graphicsView.setScene( self.scene2 )



    def limpiar(self):
        print("Limpiar")     
        self.scene.clear()

    def wheelEvent(self, event):
        if( event.delta()>0 ):
            self.ui.graphicsView.scale( 1.2, 1.2)
        else:
            self.ui.graphicsView.scale( 0.8, 0.8 )


    def dibujar(self):
        print("Dibujar")

        for particula in self.acelerador:
            pen = QPen()
            pen.setWidth( 2 )
            r = particula.red
            g = particula.green
            b = particula.blue
            color = QColor( r,g,b )
            pen.setColor( color )

            oriX = particula.origenX
            oriY = particula.origenY
            desX = particula.destinoX
            desY = particula.destinoY

            self.scene.addEllipse( oriX, oriY, 5, 5, pen )
            self.scene.addEllipse( desX, desY, 5, 5, pen )
            self.scene.addLine( oriX, oriY, desX, desY, pen )


    def ordenarId(self):
        print("Ordenando por id")
        self.acelerador.sortById()



    def ordenarVelocidad(self):
        print("Ordenando por distancia")
        self.acelerador.sortBySpeed()

    def mostrarTabla(self):
        print("Mostrar tabla")
        self.ui.table.setColumnCount( 10 )
        headers = ["Id", "origenX", "origenY", "destinoX", "destinoY", "velocidad", "distancia" ,"red", "green", "blue"]
        self.ui.table.setHorizontalHeaderLabels(headers)

        self.ui.table.setRowCount(len(self.acelerador))
        row = 0
        for particula in self.acelerador:
            self.ui.table.setRowCount( len(self.acelerador) )

            id = QTableWidgetItem( str(particula.id) )
            origenX = QTableWidgetItem( str(particula.origenX) ) 
            origenY = QTableWidgetItem( str(particula.origenY) )
            destinoX = QTableWidgetItem( str(particula.destinoX) )
            destinoY = QTableWidgetItem( str(particula.destinoY) )
            velocidad = QTableWidgetItem( str(particula.velocidad) )
            distancia = QTableWidgetItem( str(particula.distancia) )
            red = QTableWidgetItem( str(particula.red) )
            green = QTableWidgetItem( str(particula.green) )
            blue = QTableWidgetItem( str(particula.blue) ) 

            self.ui.table.setItem( row, 0, id )
            self.ui.table.setItem( row, 1, origenX )
            self.ui.table.setItem( row, 2, origenY )
            self.ui.table.setItem( row, 3, destinoX )
            self.ui.table.setItem( row, 4, destinoY )
            self.ui.table.setItem( row, 5, velocidad )
            self.ui.table.setItem( row, 6, distancia )
            self.ui.table.setItem( row, 7, red )
            self.ui.table.setItem( row, 8, green )
            self.ui.table.setItem( row, 9, blue )
            row += 1
            


    def buscar(self):
        print("Buscar")
        idBusqueda = self.ui.buscar_lineEdit.text()

        for particula in self.acelerador:
            if(idBusqueda == str(particula.id)):
                self.ui.table.clear()
                self.ui.table.setRowCount(1)

                distanciaEu = str(distancia_euclidiana( particula.origenX, particula.origenY, particula.destinoX, particula.destinoY))

                id = QTableWidgetItem( str(particula.id) )
                origenX = QTableWidgetItem( str(particula.origenX) ) 
                origenY = QTableWidgetItem( str(particula.origenY) )
                destinoX = QTableWidgetItem( str(particula.destinoX) )
                destinoY = QTableWidgetItem( str(particula.destinoY) )
                velocidad = QTableWidgetItem( str(particula.velocidad) )
                distancia = QTableWidgetItem( distanciaEu )
                red = QTableWidgetItem( str(particula.red) )
                green = QTableWidgetItem( str(particula.green) )
                blue = QTableWidgetItem( str(particula.blue) ) 

                self.ui.table.setItem( 0, 0, id )
                self.ui.table.setItem( 0, 1, origenX )
                self.ui.table.setItem( 0, 2, origenY )
                self.ui.table.setItem( 0, 3, destinoX )
                self.ui.table.setItem( 0, 4, destinoY )
                self.ui.table.setItem( 0, 5, velocidad )
                self.ui.table.setItem( 0, 6, distancia )
                self.ui.table.setItem( 0, 7, red )
                self.ui.table.setItem( 0, 8, green )
                self.ui.table.setItem( 0, 9, blue )

                return

        QMessageBox.warning(self, "ID no encontrado", "No se pudo encontrar el ID ingresado")




    def guardar( self ):
        print("Guardao")
        ubicacion = QFileDialog.getSaveFileName( self, "Guardar Particulas", ".", "JSON (*.json)" )
        print( ubicacion[0] )

        try:        
            self.acelerador.guardar( ubicacion[0] )
            QMessageBox.information(self, "Exito", "Se guardo correctamente")
        except:
            QMessageBox.critical(self, "Error", "Ocurrio un error")


    def abrir( self ):
        ubicacion = QFileDialog.getOpenFileName(self, "Abrir acelerador", ".", "JSON (*.json)")[0]        

        try:
            self.acelerador.abrir( ubicacion )
            QMessageBox.information(self, "Exito", "Se abrio correctamente")
        except:
            QMessageBox.critical(self, "Error", "Ocurrio un error al abrir")


    def clickEnviarInicio(self):
        id = self.ui.id_spinBox.value()
        origenX = self.ui.origenX_spinBox.value()
        origenY = self.ui.origenY_spinBox.value()
        destinoX = self.ui.destinoX_spinBox.value()
        destinoY = self.ui.destinoY_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()
        self.acelerador.agregar_inicio( 
            Particula( id, origenX, origenY, destinoX, destinoY, velocidad, red, green, blue ) ) 
        self.clearData()


    def clickEnviarFinal(self):
        id = self.ui.id_spinBox.value()
        origenX = self.ui.origenX_spinBox.value()
        origenY = self.ui.origenY_spinBox.value()
        destinoX = self.ui.destinoX_spinBox.value()
        destinoY = self.ui.destinoY_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()
        self.acelerador.agregar_final( 
            Particula( id, origenX, origenY, destinoX, destinoY, velocidad, red, green, blue ) ) 
        self.clearData()


    def mostrar(self):
        self.ui.salida_plainTextEdit.clear()
        # self.ui.salida_plainTextEdit.insertPlainText( str( self.acelerador ) + "\n" )
        self.ui.salida_plainTextEdit.insertPlainText( str( self.acelerador.diccionario ) + "\n" )

        # for key, value in self.acelerador.diccionario.items():
        #     pares = str(key) + " : \n" + str(value) + "\n"
        #     self.ui.salida_plainTextEdit.insertPlainText(str(pares))
        #     self.ui.salida_plainTextEdit.insertPlainText( "\n" )

    def mostrarJson(self):
        self.limpiar()
        self.dibujar()
        self.ui.salida_plainTextEdit.clear()
        for key, value in self.acelerador.diccionario.items():
            pares = str(key) + " : \n" + str(value) + "\n"
            self.ui.salida_plainTextEdit.insertPlainText(str(pares))
            self.ui.salida_plainTextEdit.insertPlainText( "\n" )

    
    def convertToDic(self):
        pen2 = QPen()
        pen2.setWidth(2)

        d = {}
        anterior = [0,0,0]
        it = 1

        for particula in self.acelerador:
            # código para mostrar en plain text edit
            self.ui.salida_plainTextEdit.clear()
            self.ui.salida_plainTextEdit.insertPlainText( pprint( self.acelerador) )

            # código lista de adyacencia
            if anterior[0] == 0:
                d[(particula.origenX, particula.origenY)] = ( str(particula.destinoX), str(particula.destinoY), str(particula.distancia) )
            else:
                d[(particula.origenX, particula.origenY)] = ( str(anterior[str(particula.destinoX)]), str(anterior[str(particula.destinoY)]), str(anterior[str(particula.distancia)]) )
            if it == len( self.acelerador ):
                d[(str(particula.destinoX), str(particula.destinoY))] = ( str(particula.origenX), str(particula.origenY), str(particula.distancia) )
            anterior[0] = str( particula.origenX )
            anterior[1] = str( particula.origenY )
            anterior[2] = str( particula.distancia )
            it += 1

        # Insertar en plain text
        for key , value in d.items():
            m = key, value
            self.ui.salida_plainTextEdit.insertPlainText( str(m) )
            self.ui.salida_plainTextEdit.insertPlainText( '\n' )


    def clearData(self):
        self.ui.id_spinBox.clear()
        self.ui.origenX_spinBox.clear()
        self.ui.origenY_spinBox.clear()
        self.ui.destinoX_spinBox.clear()
        self.ui.destinoY_spinBox.clear()
        self.ui.velocidad_spinBox.clear()
        self.ui.red_spinBox.clear()
        self.ui.green_spinBox.clear()
        self.ui.blue_spinBox.clear()