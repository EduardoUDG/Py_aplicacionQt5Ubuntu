from ui_mainwindow import Ui_MainWindow
from PySide2.QtWidgets import QFileDialog, QMainWindow, QMessageBox
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