"""
Ejercicio 2
------------------------

Módulo de funciones booleanas que, a partir de una matriz, retornan true o false.

Funciones:
---------------------
- es_canal_sin_ruido(matriz_canal: Matriz[float]) -> bool
- es_canal_determinante(matriz_canal: Matriz[float]) -> bool
"""

from algebra_lineal.Matriz import Matriz

def es_canal_sin_ruido(matriz_canal: Matriz[float]) -> bool:
    """
    Devuelve true si la matriz corresponde a un canal sin ruido, es decir, si cada columna tiene un único valor distinto de 0.

    Parámetros:
    ------------------
    - matriz_canal (Matriz[float]): Matriz que representa el canal de comunicación.

    Retorna:
    -----------------
    - bool: True si el canal es sin ruido, False en caso contrario.
    """
    N = matriz_canal.cantidadFilas
    M = matriz_canal.cantidadColumnas
    j = 0
    respuesta = True
    while j<M and respuesta:
        contador_valores_distintos_de_cero = 0
        i = 0
        while i<N and contador_valores_distintos_de_cero <= 1:
            if matriz_canal[i][j] != 0:
                contador_valores_distintos_de_cero += 1
            i += 1
        if contador_valores_distintos_de_cero != 1:
            respuesta = False
        j += 1
    return respuesta

def es_canal_determinante(matriz_canal: Matriz[float]) -> bool:
    """Devuelve true si la matriz corresponde a un canal determinante, es decir, si cada fila tiene un único valor distinto de 0.
    
    Parámetros:
    ------------------
    - matriz_canal (Matriz[float]): Matriz que representa el canal de comunicación.
    
    Retorna:
    -----------------
    - bool: True si el canal es determinante, False en caso contrario.
    """
    N = matriz_canal.cantidadFilas
    M = matriz_canal.cantidadColumnas
    i = 0
    respuesta = True
    while i<N and respuesta:
        contador_valores_distintos_de_cero = 0
        j = 0
        while j<M and contador_valores_distintos_de_cero <= 1:
            if matriz_canal[i][j] != 0:
                contador_valores_distintos_de_cero += 1
            j += 1
        if contador_valores_distintos_de_cero != 1:
            respuesta = False
        i += 1
    return respuesta