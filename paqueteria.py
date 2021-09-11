from paquete import Paquete
class Paqueteria:
    
    def __init__(self):
        self.paquetes = []

    def mostrar(self):
        for e in self.paquetes:
            e.imprimir()

    def agregar(self,paquete:Paquete):
        self.paquetes.append(paquete)

    def __str__(self) -> str:
        # strAll = ""
        # for e in self.paquetes:
        #     strAll += str(e) + "\n"
        # return strAll
 
        # join recibe una lista iterable de strings
        # antes del for indicamos lo que queremos 
        # hacer con cada elemento

        return "\n".join( str(e) for e in self.paquetes )