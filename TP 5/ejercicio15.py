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