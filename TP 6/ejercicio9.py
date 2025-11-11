"""Ejercicio 9 - TP 6
-----------------------------
Módulo con funciones que tienen, como fin, calcular capacidad de un canal.

Autor: Carlos Andrés Efstratiadis

Funciones:
---------------
- es_uniforme: Determina si un canal es uniforme.
- capacidad_canal: Calcula la capacidad de un canal de comunicación."""

from math import log2
from algebra_lineal.Matriz import Matriz
from Utils import entropia
from ejercicio2 import es_canal_determinante, es_canal_sin_ruido

def es_uniforme(matriz: Matriz) -> bool:
    """Determina si un canal es uniforme.

    Un canal es uniforme si todas las filas de su matriz contienen los mismo números.

    Parámetros:
    -----------
    matriz : Matriz
        Matriz de transición del canal.

    Retorna:
    --------
    bool
        True si el canal es uniforme, False en caso contrario.
    """
    primera_fila = matriz[0]
    for i in range(1, matriz.cantidadFilas):
        for j in range(matriz.cantidadColumnas):
            if matriz[i][j] not in primera_fila:
                return False
    return True

def capacidad_canal(matriz: Matriz) -> float:
    """
    Determina la capacidad de un canal de comunicación.

    La capacidad de un canal es la máxima cantidad de información que puede ser transmitida.

    Parámetros:
    -----------
    matriz : Matriz
        Matriz de transición del canal.

    Retorna:
    --------
    float
        Capacidad del canal.
    """
    if es_canal_determinante(matriz):
        return log2(matriz.cantidadColumnas)
    else:
        if es_canal_sin_ruido(matriz):
            return log2(matriz.cantidadFilas)
        if es_uniforme(matriz):
            return log2(matriz.cantidadColumnas) - entropia(matriz[0])
        else:
            raise ValueError("No se pudo clasificar el canal")
