"""
Ejercicio 10 - TP 6
-----------------------
Módulo con una función:
- maximizar_informacion_mutua: función que calcula capacidad y probabilidad óptima
"""

from algebra_lineal.Matriz import Matriz
from Utils import get_informacion_mutua

def maximizar_informacion_mutua(canal: Matriz[float], h: float) -> tuple[float, float]:
    """
    Calcula la capacidad de un canal binario y la probabilidad óptima de entrada

    Args:
        canal (Matriz[float]): Matriz de transición del canal binario.
        h (float): Paso.
    
    Returns:
        tuple[float, float]: probabilidad óptima de entrada y capacidad del canal.
    """
    capacidad = -1.0
    omega = 0.0
    while omega <= 1.0:
        p_apriori = [omega], [1 - omega]
        info_mutua = get_informacion_mutua(canal, p_apriori)
        if info_mutua > capacidad:
            capacidad = info_mutua
            probabilidad_optima = omega
        omega += h
    return probabilidad_optima, capacidad