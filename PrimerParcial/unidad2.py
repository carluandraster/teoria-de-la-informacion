import math
from Matriz import Matriz

def cantidadInformacion(p: float, r=2) -> float:
    """
    Calcula la cantidad de información de un evento dado su probabilidad.
    
    Parámetros:
        p (float): La probabilidad del evento (0 < p <= 1).
        r (int): La base del logaritmo (default 2).
    Retorna:
        float: La cantidad de información en bits.
    """
    if p <= 0 or p > 1:
        resultado = 0
    else:
        resultado = math.log(1/p, r)
    return resultado

def entropia(probabilidades: list, r=2) -> float:
    """
    Calcula la entropía de una fuente de información dada una lista de probabilidades.
    
    Parámetros:
        probabilidades (list): Lista de probabilidades de los eventos.
        r (int): Base del logaritmo (default 2).
    Retorna:
        float: La entropía en la unidad que corresponda (por defecto, en bits).
    """
    H = 0
    for p in probabilidades:
        H += p * cantidadInformacion(p, r)
    return H

def getAlfaProbabilidades(texto: str):
    """
    Dada una cadena de caracteres, devuelve una lista con su alfabeto y una lista con sus probabilidades.
    
    Parámetros:
        texto (str): La cadena de caracteres.
    Retorna:
        tuple: Una tupla que contiene una lista con el alfabeto y una lista con sus probabilidades.
    """
    alfabeto = []
    probabilidades = []
    longitud = len(texto)
    for simbolo in texto:
        if simbolo in alfabeto:
            index = alfabeto.index(simbolo)
            probabilidades[index] += 1
        else:
            alfabeto.append(simbolo)
            probabilidades.append(1)
    for i in range(len(probabilidades)):
        probabilidades[i] /= longitud
    return alfabeto, probabilidades