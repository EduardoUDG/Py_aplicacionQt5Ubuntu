from paquete import Paquete
from paqueteria import Paqueteria

paquete1 = Paquete('1', 'A', 'B', 0.5)
paquete2 = Paquete('1', 'B', 'C', 0.7)

sedex = Paqueteria()
# paquete.imprimir()

sedex.agregar( paquete1 );
sedex.agregar( paquete2 );

print( sedex )