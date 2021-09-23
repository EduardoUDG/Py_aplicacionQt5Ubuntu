
from models.particula import Particula
import json
class StartLabs:

    def __init__(self):
        self.__particulas = []

    def agregar_final(self, particula:Particula):
        self.particulas.append( particula )

    def agregar_inicio(self, particula:Particula):
        self.particulas.insert( 0, particula )

    def __str__(self) -> str:
        return "\n".join( str(e) for e in self.particulas )

    def __len__(self):
        return len( self.__particulas )

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        if self.count < len( self.__particulas ):
            particula = self.__particulas[self.count]
            self.count += 1
            return particula
        else:
            raise StopIteration


    def guardar(self, ubicacion):
        # archivo = open( ubicacion, 'w' )

        with open(ubicacion,'w') as archivo:
            # archivo.write( str(self) )
            listaDic = [ e.to_json() for e in self.particulas ]
            json.dump( listaDic, archivo, indent=5 )

    
    def abrir(self, ubicacion):
        with open(ubicacion,'r') as archivo:
            listaDic = json.load( archivo )

            self.particulas = [ Particula(**e) for e in listaDic ]