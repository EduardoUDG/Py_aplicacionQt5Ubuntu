from models.algoritmos import distancia_euclidiana


class Particula:
    def __init__(
        self, id, origenX, origenY, destinoX, destinoY, velocidad, red, green, blue
    ):

        self.__id = id
        self.__origenX = origenX
        self.__origenY = origenY
        self.__destinoX = destinoX
        self.__destinoY = destinoY
        self.__velocidad = velocidad
        self.__red = red
        self.__green = green
        self.__blue = blue
        self.__distancia = distancia_euclidiana( self.__origenX, self.__origenY, self.__destinoX, self.__destinoY )


    def __str__(self) -> str:
        return (
            " Particula: "
            + str(self.__id)
            + " origenX: "
            + str(self.__origenX)
            + " origenY: "
            + str(self.__origenY)
            + " destinoX: "
            + str(self.__destinoX)
            + " destinoY: "
            + str(self.__destinoY)
            + " velocidad: "
            + str(self.__velocidad)
            + " red: "
            + str(self.__red)
            + " green: "
            + str(self.__green)
            + " blue: "
            + str(self.__blue)
        )

    def to_json(self):
        return {
            "id": self.__id,
            "origenX": self.__origenX,
            "origenY": self.__origenY,
            "destinoX": self.__destinoX,
            "destinoY": self.__destinoY,
            "velocidad": self.__velocidad,
            "red": self.__red,
            "green": self.__green,
            "blue": self.__blue
        }

    def to_dic(self):
        return {
            "id": self.__id,
            "origenX": self.__origenX,
            "origenY": self.__origenY,
            "destinoX": self.__destinoX,
            "destinoY": self.__destinoY,
            "velocidad": self.__velocidad,
            "red": self.__red,
            "green": self.__green,
            "blue": self.__blue,
            "distancia": self.__distancia
        }

    def __lt__( self, other ):
        return  self.id < other.id

    @property
    def id(self):
        return self.__id
    
    @property
    def origenX(self):
        return self.__origenX

    @property
    def origenY(self):
        return self.__origenY

    @property
    def destinoX(self):
        return self.__destinoX

    @property
    def destinoY(self):
        return self.__destinoX

    @property
    def velocidad(self):
        return self.__velocidad

    @property
    def red(self):
        return self.__red

    @property
    def green(self):
        return self.__green

    @property
    def blue(self):
        return self.__blue

    @property
    def distancia(self):
        return self.__distancia


    # @origenX.setter
    # def origenX(self, newOrigenX ):
    #     if newOrigenX > 0:
    #         self.__origenX = newOrigenX
    #     else:
    #         self.__origenX = 1

