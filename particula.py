from algoritmos  import distancia_euclidiana

class Particula:
    
    def __init__(self, 
            id, 
            origenX, 
            origenY, 
            destinoX, 
            destinoY, 
            velocidad, 
            red, 
            green, 
            blue):

        self.id = id
        self.origenX = origenX
        self.origenY = origenY
        self.destinoX = destinoX
        self.destinoY = destinoY
        self.velocidad = velocidad
        self.red = red
        self.green = green
        self.blue = blue


    def distancia(self)->float:
        x_1 = self.origenX
        x_2 = self.destinoX
        y_1 = self.origenY
        y_2 = self.destinoY
        
        return distancia_euclidiana( x_1, y_1, x_2, y_2 )

    def __str__(self) -> str:
        return ("Particula " + str(self.id) + 
            " origenX " + str(self.origenX) +
            " origenY " + str(self.origenY) +
            " destinoX " + str(self.destinoX) +
            " destinoY " + str(self.destinoY) +
            " red " + str(self.red) +
            " green " + str(self.green) +
            " blue " + str(self.blue) 
        )
            
    