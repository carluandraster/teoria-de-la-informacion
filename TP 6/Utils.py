"""Utils
------------------------------

Módulo que contiene funciones para calcular diversas métricas de un canal de comunicación.

Funciones:
--------------------
- entropia_a_posteriori(probabilidades_a_priori: list[float], matriz_de_canal: Matriz[float]) -> list[float]
- get_probabilidades_salidas(probabilidades_a_priori: list[float], matriz_canal: Matriz[float]) -> list[float]
- get_probabilidades_a_posteriori(probabilidades_a_priori: list[float], matriz_canal: Matriz[float]) -> Matriz[float]
- get_probabilidades_eventos_simultaneos(probabilidades_a_priori: list[float], matriz_canal: Matriz[float]) -> Matriz[float]
- cantidadInformacion(p: float, r=2) -> float
- entropia(probabilidades: list, r=2) -> float
- get_ruido(probs_a_priori: list[float], probs_condicionales: Matriz[float]) -> float
- get_perdida(probs_a_priori: list[float], probs_condicionales: Matriz[float]) -> float
- get_entropia_afin(probs_a_priori: list[float], probs_condicionales: Matriz[float]) -> float
- get_informacion_mutua(probs_a_priori: list[float], probs_condicionales: Matriz[float]) -> float
"""

import math
from algebra_lineal.Matriz import Matriz
from algebra_lineal import MatrizFactory as mf

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

def get_ruido(probs_a_priori: list[float], probs_condicionales: Matriz[float])->float:
    """Calcula el ruido de un canal de comunicacion.

    Args:
        probs_a_priori (list[float]): Probabilidades a priori de los eventos de entrada.
        probs_condicionales (Matriz[float]): Matriz de probabilidades condicionales del canal.

    Returns:
        float: Ruido del canal.
    """
    probs_salidas = get_probabilidades_salidas(probs_a_priori, probs_condicionales)
    H_A_given_b = entropia_a_posteriori(probs_a_priori, probs_condicionales)
    H_A_given_B = 0
    for p, h in zip(probs_salidas, H_A_given_b):
        H_A_given_B += p * h
    return H_A_given_B

def get_perdida(probs_a_priori: list[float], probs_condicionales: Matriz[float])->float:
    """Calcula la perdida de un canal de comunicacion.

    Args:
        probs_a_priori (list[float]): Probabilidades a priori de los eventos de entrada.
        probs_condicionales (Matriz[float]): Matriz de probabilidades condicionales del canal.

    Returns:
        float: Perdida del canal.
    """
    H_A_given_B = get_ruido(probs_a_priori, probs_condicionales)
    H_A = entropia(probs_a_priori)
    H_B = entropia(get_probabilidades_salidas(probs_a_priori, probs_condicionales))
    return H_A_given_B + H_B - H_A

def get_entropia_afin(probs_a_priori: list[float], probs_condicionales: Matriz[float])->float:
    """Calcula la entropia afin de un canal de comunicacion.

    Args:
        probs_a_priori (list[float]): Probabilidades a priori de los eventos de entrada.
        probs_condicionales (Matriz[float]): Matriz de probabilidades condicionales del canal.

    Returns:
        float: Entropia afin del canal.
    """
    P_a_b = get_probabilidades_eventos_simultaneos(probs_a_priori, probs_condicionales)
    entropia_afin = 0
    for fila in P_a_b:
        entropia_afin += entropia(fila)
    return entropia_afin

def get_informacion_mutua(probs_a_priori: list[float], probs_condicionales: Matriz[float])->float:
    """Calcula la informacion mutua de un canal de comunicacion.

    Args:
        probs_a_priori (list[float]): Probabilidades a priori de los eventos de entrada.
        probs_condicionales (Matriz[float]): Matriz de probabilidades condicionales del canal.

    Returns:
        float: Informacion mutua del canal.
    """
    P = get_probabilidades_eventos_simultaneos(probs_a_priori, probs_condicionales)
    informacion_mutua = 0
    probs_salidas = get_probabilidades_salidas(probs_a_priori, probs_condicionales)
    for a in range(len(probs_a_priori)):
        for b in range(len(probs_salidas)):
            if(P[a][b] > 0):
                informacion_mutua += P[a][b] * math.log2(P[a][b] / (probs_a_priori[a] * probs_salidas[b]))
    return informacion_mutua