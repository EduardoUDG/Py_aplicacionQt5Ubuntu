
from models.particula import Particula
from pprint import pprint
import json
class StartLabs:

    def __init__(self):
        self.__particulas = []
        self.Dparticulas= {}

    def agregar_final(self, particula:Particula):
        print("Agregando particula al final")
        self.__particulas.append( particula )
        origenX = particula.origenX
        origenY = particula.origenY
        destinoX = particula.destinoX
        destinoY = particula.destinoY
        distancia = particula.distancia

        key     = (origenX,origenY)
        value   = (destinoX,destinoY,distancia)


        print( self.Dparticulas )



    def agregar_inicio(self, particula:Particula):
        print("Agregando particula al final")
        self.__particulas.insert( 0, particula )


    def __str__(self) -> str:
        return "".join( str(e)+"\n" for e in self.__particulas )

    def __len__(self):
        return len( self.__particulas )

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        if self.count<len(self.__particulas):
            particula = self.__particulas[self.count]
            self.count += 1
            return particula
        else:
            raise StopIteration


    def sortById( self ):
        return self.__particulas.sort()

    def sortBySpeed( self ):
        return self.__particulas.sort( key=lambda particula:particula.velocidad)


    def guardar(self, ubicacion):
        # archivo = open( ubicacion, 'w' )
        try:
            with open(ubicacion,'w') as archivo:
                # archivo.write( str(self) )
                listaDic = [ e.to_json() for e in self.__particulas ]
                json.dump( listaDic, archivo, indent=5 )
            return True
        except:
            return False
    
    def abrir(self, ubicacion):
        try:
            with open(ubicacion,'r') as archivo:
                listaDic = json.load( archivo )

                self.__particulas = [ Particula(**e) for e in listaDic ]
            return 1
        except:
            return 0