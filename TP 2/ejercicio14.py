from Matriz import Matriz
import MatrizFactory as mf
import Utils

def estadosEstables(matriz: Matriz[float]) -> Matriz[float]:
    """
    Calcula la matriz de estados estables de una cadena de Markov dada su matriz de transición.
    
    Parámetros:
        matriz (Matriz[float]): La matriz de transición de la cadena de Markov.
    Retorna:
        Matriz[float]: La matriz de estados estables.
    Lanza:
        ValueError: Si la matriz no es cuadrada.
    """
    if matriz.cantidadFilas != matriz.cantidadColumnas:
        raise ValueError("La matriz debe ser cuadrada para calcular los estados estables.")

    n = matriz.cantidadFilas
    A = matriz - mf.identidad(n)

    for j in range(n):
        A[n-1][j] = 1.0

    b = mf.ceros(n, 1)
    b[n-1][0] = 1.0

    return A.inversa * b

def entropiaMarkoviana(matriz: Matriz[float]) -> float:
    """
    Calcula la entropía markoviana de una cadena de Markov dada su matriz de transición.
    
    Parámetros:
        matriz (Matriz[float]): La matriz de transición de la cadena de Markov.
    Retorna:
        float: La entropía markoviana.
    Lanza:
        ValueError: Si la matriz no es cuadrada.
    """
    if matriz.cantidadFilas != matriz.cantidadColumnas:
        raise ValueError("La matriz debe ser cuadrada para calcular la entropía markoviana.")
    estados = estadosEstables(matriz)
    H = 0
    for i in range(matriz.cantidadColumnas):
        columna = matriz.getColumna(i)
        H += estados[i][0] * Utils.entropia(columna)
    return H