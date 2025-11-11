"""Ejercicio 9 - TP 6
-----------------------------
Módulo con funciones que tienen, como fin, calcular capacidad de un canal.

Autor: Carlos Andrés Efstratiadis

Funciones:
---------------
- es_uniforme: Determina si un canal es uniforme.
- capacidad_canal: Calcula la capacidad de un canal de comunicación."""

from algebra_lineal.Matriz import Matriz

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
        if matriz[i] not in primera_fila:
            return False
    return True