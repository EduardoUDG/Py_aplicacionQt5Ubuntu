

class Particula:
    
    def __init__(self, 
            id:int, 
            origenX:int, 
            origenY:int, 
            destinoX:int, 
            destinoY:int, 
            velocidad:int, 
            red:int, 
            green:int, 
            blue:int):
        self.id = id
        self.origenX = origenX
        self.origenY = origenY
        self.destinoX = destinoX
        self.destinoY = destinoY
        self.velocidad = velocidad
        self.red = red
        self.green = green
        self.blue = blue