from Matriz import Matriz
import MatrizFactory as mf
import Utils

# Función que, a partir de una matriz de transición, devuelve la matriz de estados estables
def estadosEstables(matriz: Matriz[float]) -> Matriz[float]:
    if matriz.cantidadFilas != matriz.cantidadColumnas:
        raise ValueError("La matriz debe ser cuadrada para calcular los estados estables.")

    n = matriz.cantidadFilas
    A = matriz - mf.identidad(n)

    for j in range(n):
        A[n-1][j] = 1.0

    b = mf.ceros(n, 1)
    b[n-1][0] = 1.0

    return A.inversa * b

# Devuelve la entropía de una fuenta markoviana
def entropiaMarkoviana(matriz: Matriz[float]) -> float:
    estados = estadosEstables(matriz)
    H = 0
    for i in range(matriz.cantidadColumnas):
        columna = matriz.getColumna(i)
        H += estados[i][0] * Utils.entropia(columna)
    return H