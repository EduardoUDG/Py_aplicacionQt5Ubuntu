import math

def distancia_euclidiana(x_1, y_1, x_2, y_2)->float:
    resolve = ( (x_2-x_1)**2 + (y_2-y_1)**2 )
    resultado = float( math.sqrt( resolve ) )

    return resultado