import math
from ejercicio9 import get_alfabeto_codigo

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
    r = len(get_alfabeto_codigo(codigos))
    for codigo, probabilidad in zip(codigos, probabilidades):
        longitud_codigo = len(codigo)
        limite_superior = math.ceil(-math.log(probabilidad, r))
        if longitud_codigo > limite_superior:
            return False
    return True