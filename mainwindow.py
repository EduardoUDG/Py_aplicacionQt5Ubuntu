from models.algoritmos import distancia_euclidiana
from ui_mainwindow import Ui_MainWindow
from PySide2.QtWidgets import QFileDialog, QMainWindow, QMessageBox, QTableWidgetItem
from models.particula import Particula
from models.startLabs import StartLabs

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

        self.ui.buscar_pushButton.clicked.connect( self.buscar )
        self.ui.mostrarTabla_pushButton.clicked.connect( self.mostrarTabla )



    def mostrarTabla(self):
        print("Mostrar tabla")
        self.ui.table.setColumnCount( 10 )
        headers = ["Id", "origenX", "origenY", "destinoX", "destinoY", "velocidad", "distancia" ,"red", "green", "blue"]
        self.ui.table.setHorizontalHeaderLabels(headers)

        self.ui.table.setRowCount(len(self.acelerador))
        row = 0
        for particula in self.acelerador:
            self.ui.table.setRowCount( len(self.acelerador) )
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
        self.ui.salida_plainTextEdit.insertPlainText( str( self.acelerador ) + "\n" )


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