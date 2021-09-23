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

    def distancia(self) -> float:
        x_1 = self.__origenX
        x_2 = self.__destinoX
        y_1 = self.__origenY
        y_2 = self.__destinoY

        return distancia_euclidiana(x_1, y_1, x_2, y_2)

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
            + "\n"
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
            "blue": self.__blue,
        }

    
    @property
    def id(self):
        return self.__id
    
    @property
    def origenX(self):
        return self.__origenX

    @origenX.setter
    def origenX(self, newOrigenX ):
        if newOrigenX > 0:
            self.__origenX = newOrigenX
        else:
            self.__origenX = 1
