"""
Ejercicio 4
------------------------------
Módulo con una única función para calcular la matriz compuesta de dos canales de comunicación:
get_matriz_compuesta(canal1: Matriz, canal2: Matriz) -> Matriz"""

from algebra_lineal.Matriz import Matriz

def get_matriz_compuesta(canal1: Matriz[float], canal2: Matriz[float]) -> Matriz[float]:
    """Calcula la matriz compuesta de dos canales de comunicación.

    Args:
        canal1 (Matriz): Matriz de transición del primer canal.
        canal2 (Matriz): Matriz de transición del segundo canal.

    Returns:
        Matriz: Matriz de transición del canal compuesto.
    """
    return canal1 * canal2	