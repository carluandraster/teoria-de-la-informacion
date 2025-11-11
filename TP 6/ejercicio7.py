"""TP 6 - Ejercicio 7
Implementar una función que reduzca una matriz de canal combinando columnas
cuando sea posible sin perder información. La función debe iterar hasta que no
se puedan realizar más combinaciones.

Autor: Carlos Andrés Efstratiadis

Funciones:
---------------
    reducir_matriz: Combina de a 2 columnas de la matriz hasta que no se puedan
                     reducir más sin perder información."""

from ejercicio6 import se_pueden_reducir, generar_matriz_determinante
from algebra_lineal.Matriz import Matriz

def reducir_matriz(matriz: Matriz[float])->Matriz[float]:
    """
    Combina de a 2 columnas de la matriz hasta que no se puedan reducir más sin perder información.
    
    Args:
        matriz (Matriz[float]): Matriz a reducir.
    Returns:
        Matriz[float]: Matriz reducida.
    """
    matriz_reducida = matriz.clone
    i = 0
    j = 1
    n = matriz_reducida.cantidadColumnas
    while i < n or j < n:
        if se_pueden_reducir(matriz_reducida, i, j):
            matriz_determinante = generar_matriz_determinante(matriz_reducida, i, j)
            matriz_reducida *= matriz_determinante
            n -= 1
            i = 0
            j = 1
        else:
            j += 1
            if j == n:
                i += 1
                j = i + 1
    return matriz_reducida