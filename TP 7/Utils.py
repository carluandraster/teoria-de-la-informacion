import math

def cantidadInformacion(p: float, r: int=2) -> float:
    """Dada una probabilidad, calcula la cantidad de información.

    Parámetros:	
        p (float): probabilidad del evento (0 < p <= 1).
        r (int): base del logaritmo (default 2).
    
    Retorna:
        float: la cantidad de información en bits (si r=2).
    """
    if p <= 0 or p > 1:
        resultado = 0
    else:
        resultado = math.log(1/p, r)
    return resultado

def entropia(probabilidades: list[float], r: int=2) -> float:
    """Calcula la entropía de una lista de probabilidades.

    Parámetros:
        probabilidades (list[float]): lista de probabilidades de los eventos.
        r (int): base del logaritmo (default 2).
    
    Retorna:
        float: la entropía en bits (si r=2).
    """
    h: float = 0.0
    for p in probabilidades:
        h += p * cantidadInformacion(p, r)
    return h

def funcion_entropia(omega: float, r: int=2) -> float:
    """Calcula la función de entropía para una probabilidad omega.

    Parámetros:
        omega (float): probabilidad del evento (0 < omega <= 1).
        r (int): base del logaritmo (default 2).
    
    Retorna:
        float: el valor de la función de entropía en bits (si r=2).
    """
    if omega <= 0 or omega > 1:
        resultado = 0
    else:
        resultado = entropia([omega, 1 - omega], r)
    return resultado