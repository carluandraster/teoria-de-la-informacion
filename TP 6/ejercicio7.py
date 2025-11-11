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
    