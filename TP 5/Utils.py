"""Módulo de utilidades para el cálculo de frecuencias, cantidades de información y entropía.

Funciones:
---------------
- <b>get_frecuencias(texto: str) -> dict[str, int]:</b> Calcula la frecuencia de cada carácter en un texto.
- <b>get_frecuencias_relativas(texto: str) -> dict[str, float]:</b> Calcula la frecuencia relativa de cada carácter en un texto.
- <b>cantidadInformacion(p: float, r=2) -> float:</b> Calcula la cantidad de información de un evento dado su probabilidad.
- <b>entropia(probabilidades: list, r=2) -> float:</b> Calcula la entropía de una fuente de información dada una lista de probabilidades.
"""

import math



def get_frecuencias(texto: str)-> dict[str, int]:
    """
    Esta función recibe un texto y devuelve un diccionario con la frecuencia de cada carácter en el texto.
    
    :param str texto: El texto del cual se quieren obtener las frecuencias de los caracteres.
    :return dict[str, int]: Un diccionario donde las claves son los caracteres y los valores son sus frecuencias.
    """
    frecuencias = {}
    for char in texto:
        if char in frecuencias:
            frecuencias[char] += 1
        else:
            frecuencias[char] = 1
    return frecuencias

def get_frecuencias_relativas(texto: str) -> dict[str, float]:
    """
    Esta función recibe un texto y devuelve un diccionario con la frecuencia relativa de cada carácter en el texto.
    
    :param str texto: El texto del cual se quieren obtener las frecuencias relativas de los caracteres.
    :return dict[str, float]: Un diccionario donde las claves son los caracteres y los valores son sus frecuencias relativas.
    """
    frecuencias = get_frecuencias(texto)
    total_caracteres = len(texto)
    frecuencias_relativas = {char: freq / total_caracteres for char, freq in frecuencias.items()}
    return frecuencias_relativas

def cantidadInformacion(p: float, r=2) -> float:
    """
    Calcula la cantidad de información de un evento dado su probabilidad.
    
    :param float p: La probabilidad del evento (0 < p <= 1).
    :param int r: La base del logaritmo (default 2).
    :return float: La cantidad de información en bits.
    """
    if p <= 0 or p > 1:
        resultado = 0
    else:
        resultado = math.log(1/p, r)
    return resultado

def entropia(probabilidades: list, r=2) -> float:
    """
    Calcula la entropía de una fuente de información dada una lista de probabilidades.
    
    :param list probabilidades: Lista de probabilidades de los eventos.
    :param int r: Base del logaritmo (default 2).
    :return float: La entropía en la unidad que corresponda (por defecto, en bits).
    """
    H = 0
    for p in probabilidades:
        H += p * cantidadInformacion(p, r)
    return H