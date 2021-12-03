
from models.particula import Particula
from pprint import pformat
import json

class StartLabs:

    def __init__(self):
        self.__particulas = []
        self.diccionario= {}
        self.__adyPonderado = {}

    def agregar_final(self, particula:Particula):
        print("Agregando particula al final")
        self.__particulas.append( particula )
        self.agregarDiccionario( particula )


    def agregar_inicio(self, particula:Particula):
        print("Agregando particula al inicio")
        self.__particulas.insert( 0, particula )
        self.agregarDiccionario(particula)


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

                self.diccionario = {}
                for particula in self.__particulas:
                    self.agregarDiccionario( particula )
            return 1
        except:
            return 0

    
    def agregarDiccionario(self, particula):
        origen = (particula.origenX, particula.origenY)
        destino = (particula.destinoX, particula.destinoY)

        if origen in self.diccionario:
            self.diccionario[origen].append((destino,particula.distancia))
        else:
            self.diccionario[origen] = [(destino,particula.distancia)]

        if destino in self.diccionario:
            self.diccionario[destino].append((origen,particula.distancia))
        else:
            self.diccionario[destino] = [(origen,particula.distancia)]

    

    def get_lista_ady_ponderada(self):
        self.__adyPonderado.clear()

        for particula in self.__particulas:
            if particula.dirigido():
                pass
            else:
                n1 = particula.get_nodo1()
                n2 = particula.get_nodo2()
                self.agregar_dict_ponderado(n1, n2, arista.peso)
                self.agregar_dict_ponderado(n2, n1, arista.peso)
        return self.__adyPonderado

    
    def print_ady_ponderada(self):
       self.get_lista_ady_ponderada()
       for key in self.__adyPonderado.keys():
           print(key, "---->", end="")
           for value in self.__adyPonderado[key]:
               nodo = value[0]
               peso = value[1]
               print(f"[{nodo}, {peso}]", "," , end="")
           print('\n')