"""Ejercicio 15
------------------------------

Módulo que contiene funciones para calcular diversas métricas de un canal de comunicación, como el ruido, la pérdida, la entropía afín y la información mutua.

Funciones:
--------------------
- get_ruido(probs_a_priori: list[float], probs_condicionales: Matriz[float]) -> float
- get_perdida(probs_a_priori: list[float], probs_condicionales: Matriz[float]) -> float
- get_entropia_afin(probs_a_priori: list[float], probs_condicionales: Matriz[float]) -> float
- get_informacion_mutua(probs_a_priori: list[float], probs_condicionales: Matriz[float]) -> float
"""

import math
from algebra_lineal.Matriz import Matriz
from Utils import entropia
from ejercicio7 import get_probabilidades_salidas, get_probabilidades_eventos_simultaneos
from ejercicio11 import entropia_a_posteriori

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