"""Ejercicio 7 de la guía 4 de Teoría de la Información.

Funciones:
---------------
- <b>get_probabilidades_salidas(probabilidades_a_priori: list[float], matriz_canal: Matriz[float]) -> list[float]:</b> Calcula las probabilidades de las salidas de un canal de comunicación.
- <b>get_probabilidades_a_posteriori(probabilidades_a_priori: list[float], matriz_canal: Matriz[float]) -> Matriz[float]:</b> Calcula las probabilidades a posteriori de las entradas dado un canal de comunicación.
- <b>get_probabilidades_eventos_simultaneos(probabilidades_a_priori: list[float], matriz_canal: Matriz[float]) -> Matriz[float]:</b> Calcula las probabilidades de eventos simultáneos de entradas y salidas en un canal de comunicación.
"""

from algebra_lineal.Matriz import Matriz
from algebra_lineal import MatrizFactory as mf

def get_probabilidades_salidas(probabilidades_a_priori: list[float], matriz_canal: Matriz[float]) -> list[float]:
    """
    Calcula las probabilidades de las salidas de un canal de comunicación.

    :param probabilidades_a_priori: Lista de probabilidades a priori de las entradas.
    :param matriz_canal: Matriz de transición del canal, donde cada elemento (i, j)
      representa la probabilidad de que la entrada i produzca la salida j.

    :return: Lista de probabilidades de las salidas.
    """
    # Convertir la lista de probabilidades a priori en una matriz columna
    matriz_entradas = Matriz([probabilidades_a_priori])
    
    # Calcular la matriz de probabilidades de salidas
    matriz_salidas = matriz_entradas * matriz_canal

    # Devolver la lista de probabilidades de las salidas
    return matriz_salidas[0]

def get_probabilidades_a_posteriori(probabilidades_a_priori: list[float], matriz_canal: Matriz[float]) -> Matriz[float]:
    """
    Calcula las probabilidades a posteriori de las entradas dado un canal de comunicación.

    :param probabilidades_a_priori: Lista de probabilidades a priori de las entradas.
    :param matriz_canal: Matriz de transición del canal, donde cada elemento (i, j)
      representa la probabilidad de que la entrada i produzca la salida j.

    :return: Matriz de probabilidades a posteriori, donde cada elemento (i, j)
      representa la probabilidad de que la entrada i haya ocurrido dado que se observó la salida j.
    """
    # Obtener las probabilidades de las salidas
    probabilidades_salidas = get_probabilidades_salidas(probabilidades_a_priori, matriz_canal)

    # Crear una matriz para las probabilidades a posteriori
    matriz_a_posteriori = mf.ceros(matriz_canal.cantidadFilas, matriz_canal.cantidadColumnas)

    # Calcular las probabilidades a posteriori usando el teorema de Bayes
    for i in range(matriz_canal.cantidadFilas):
        for j in range(matriz_canal.cantidadColumnas):
            if probabilidades_salidas[j] != 0:
                matriz_a_posteriori[i][j] = (matriz_canal[i][j] * probabilidades_a_priori[i]) / probabilidades_salidas[j]
            else:
                matriz_a_posteriori[i][j] = 0.0

    return matriz_a_posteriori

def get_probabilidades_eventos_simultaneos(probabilidades_a_priori: list[float], matriz_canal: Matriz[float]) -> Matriz[float]:
    """
    Calcula las probabilidades de eventos simultáneos de entradas y salidas en un canal de comunicación.

    :param probabilidades_a_priori: Lista de probabilidades a priori de las entradas.
    :param matriz_canal: Matriz de transición del canal, donde cada elemento (i, j)
      representa la probabilidad de que la entrada i produzca la salida j.

    :return: Matriz de probabilidades de eventos simultáneos, donde cada elemento (i, j)
      representa la probabilidad de que ocurra la entrada i y se observe la salida j.
    """
    # Crear una matriz para las probabilidades de eventos simultáneos
    matriz_eventos_simultaneos = mf.ceros(matriz_canal.cantidadFilas, matriz_canal.cantidadColumnas)

    # Calcular las probabilidades de eventos simultáneos
    for i in range(matriz_canal.cantidadFilas):
        for j in range(matriz_canal.cantidadColumnas):
            matriz_eventos_simultaneos[i][j] = matriz_canal[i][j] * probabilidades_a_priori[i]

    return matriz_eventos_simultaneos