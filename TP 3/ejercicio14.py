import math
from ejercicio5 import esInstantaneo
from ejercicio9 import get_alfabeto_codigo, get_longitudes

def es_codigo_compacto(codigos: list[str], probabilidades: list[float]) -> bool:
    """
    Determina si un conjunto de códigos es compacto.

    Un conjunto de códigos es compacto si cada longitud de código es menor o igual
    que la función techo del logaritmo en base r (donde r es el tamaño del alfabeto) de
    la inversa a la probabilidad asociada a ese código.

    Parámetros:
        codigos (list[str]): Lista de códigos.
        probabilidades (list[float]): Lista de probabilidades asociadas a cada código.

    Retorna:
        bool: True si el conjunto de códigos es compacto, False en caso contrario.
        
    Contrato:
        - codigos es distinto de None y de lista vacía
        - probabilidades es distinto de None y de lista vacía
        - len(codigos) == len(probabilidades)
        - todas las probabilidades son mayores que 0 y menores o iguales a 1
        - la suma de todas las probabilidades es igual a 1
    """
    if esInstantaneo(codigos):
        R = len(get_alfabeto_codigo(codigos))
        LONGITUDES = get_longitudes(codigos)
        i = 0
        respuesta = True
        while i < len(codigos) and respuesta:
            limite_superior = math.ceil(-math.log(probabilidades[i], R))
            if LONGITUDES[i] > limite_superior:
                respuesta = False
            i += 1
    else:
        respuesta = False
    return respuesta