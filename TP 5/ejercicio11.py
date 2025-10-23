"""Ejercicio 11 de la guía 4 de Teoría de la Información.

Funciones:
------------
- <b>entropia_a_posteriori</b>: Calcula la entropía a posteriori para cada símbolo recibido.
"""

from Utils import entropia
from ejercicio7 import get_probabilidades_a_posteriori
from algebra_lineal.Matriz import Matriz

def entropia_a_posteriori(probabilidades_a_priori: list[float], matriz_de_canal: Matriz[float]) -> list[float]:
    """Calcula la entropía a posteriori para cada símbolo recibido.

    :param list[float] probabilidades_a_priori: Probabilidades a priori de los símbolos emitidos.
    :param Matriz[float] matriz_de_canal: Matriz de canal que define las probabilidades de transición.

    :return: list[float]: Entropías a posteriori para cada símbolo recibido.
    """
    probabilidades_a_posteriori = get_probabilidades_a_posteriori(probabilidades_a_priori, matriz_de_canal)
    entropias = []
    N = probabilidades_a_posteriori.cantidadColumnas
    for i in range(N):
        entropias.append(entropia(probabilidades_a_posteriori.getColumna(i)))
    return entropias