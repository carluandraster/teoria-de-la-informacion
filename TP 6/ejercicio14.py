"""Ejercicio 14 - TP 6
-----------------------
Módulo que contiene la función para calcular la probabilidad de error de un canal

Funciones:
------------
- prob_error_canal(canal: Matriz[float]) -> float:
    Calcula la probabilidad de error de un canal utilizando la regla de decisión de máxima posibilidad."""

from algebra_lineal.Matriz import Matriz

def prob_error_canal(probs_a_priori: list[float], canal: Matriz[float]) -> float:
    """Calcula la probabilidad de error de un canal utilizando la regla de decisión de máxima posibilidad.

    Args:
        probs_a_priori (list[float]): Lista de probabilidades a priori.
        canal (Matriz[float]): Matriz de probabilidades del canal.

    Returns:
        float: La probabilidad de error del canal.
    """
    regla_de_decision = []
    for j in range(canal.cantidadColumnas):
        columna = canal.getColumna(j)
        regla_de_decision.append(columna.index(max(columna)))

    prob_error = 0.0
    for i in range(canal.cantidadFilas):
        for j in range(canal.cantidadColumnas):
            if j != regla_de_decision[i]:
                prob_error += probs_a_priori[i] * canal[i][j]

    return prob_error