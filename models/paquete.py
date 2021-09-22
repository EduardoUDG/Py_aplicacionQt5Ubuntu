class Paquete:
    def __init__(self,id,origen,destino,peso):
        self.id = id
        self.origen= origen
        self.destino = destino
        self.peso = peso

    def imprimir(self):
        print("El paquete ",self.id," va de ", self.origen, " a ", self.destino, " y pesa ",self.peso)

    def __str__(self) -> str:
        return "Paquete " + self.id + " va de " + self.origen + " a " + self.destino + " y pesa " + str(self.peso)