"""Ejercicio 6 - TP 6: Reducción de canales en una matriz de canal.
-----------------------------------------------------------------------
Implementa dos funciones para poder reducir la matriz de un canal.

Funciones:
-------------------
- se_pueden_reducir: Determina si dos canales pueden ser reducidos sin perder información.
- generar_matriz_determinante: Genera una matriz de determinante para la reducción de canales.
"""

from algebra_lineal.Matriz import Matriz
from algebra_lineal.MatrizFactory import identidad

def se_pueden_reducir(matriz_de_canal: Matriz[float], ind_columna1: int, ind_columna2: int) -> bool:
    """
    Determina si dos canales representados por las columnas `ind_columna1` y `ind_columna2` de la matriz de canal
    pueden ser reducidos (combinados) sin perder información.

    Args:
        matriz_de_canal (Matriz[float]): La matriz que representa los canales.
        ind_columna1 (int): El índice de la primera columna (canal).
        ind_columna2 (int): El índice de la segunda columna (canal).

    Returns:
        bool: True si los canales pueden ser reducidos, False en caso contrario.
    """
    columna1 = matriz_de_canal.getColumna(ind_columna1)
    columna2 = matriz_de_canal.getColumna(ind_columna2)

    # Verificar si las columnas son proporcionales
    proporcion = None
    for a, b in zip(columna1, columna2):
        if b != 0:
            ratio = a / b
            if proporcion is None:
                proporcion = ratio
            elif proporcion != ratio:
                return False
        elif a != 0:
            return False

    return True

def generar_matriz_determinante(matriz_de_canal: Matriz[float], columna1: int, columna2: int) -> Matriz[int]:
    """
    Genera una matriz de determinante para la reducción de canales.

    Args:
        matriz_de_canal (Matriz[float]): La matriz que representa los canales.
        columna1 (int): El índice de la primera columna (canal).
        columna2 (int): El índice de la segunda columna (canal).

    Returns:
        Matriz[float]: La matriz de determinante para la reducción.
    """
    columnas = matriz_de_canal.cantidadColumnas - 1
    matriz_determinante = identidad(columnas)
    fila_nueva = [0] * (columnas)
    fila_nueva[columna1] = 1
    matriz_determinante.insertar_fila(columna2, fila_nueva)

    return matriz_determinante