from PySide2.QtWidgets import QApplication
from views.mainwindow import MainWindow
import sys

# Los archvios en minusculas
# Las clases en mayusculas
# from = nombre archivo | path
# import clase, funcion, etc.

# Aplicación de Qt
app = QApplication()

# Se crea la ventana Qt
window = MainWindow()

# Se imprime la ventana Qt
window.show()

# Ejecuta nuestra app | ventana Qt
sys.exit(app.exec_())

