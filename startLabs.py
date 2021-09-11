
from particula import Particula

class StartLabs:

    def __init__(self):
        self.particulas = []

    def agregar_final(self, particula:Particula):
        self.particulas.append( particula )

    def agregar_inicio(self, particula:Particula):
        self.particulas.insert( 0, particula )

    def __str__(self) -> str:
        return "\n".join( str(e) for e in self.particulas )