from particula import Particula
from startLabs import StartLabs

particula1 = Particula(1, 100, 150, 50, 650, 50, 255, 255, 255);
particula2 = Particula(2, 10, 15, 50, 65, 5, 255, 255, 255);

dist = particula1.distancia()

acelerador = StartLabs()

acelerador.agregar_final( particula1 )
acelerador.agregar_inicio( particula2 )

print( acelerador )
print( dist )
