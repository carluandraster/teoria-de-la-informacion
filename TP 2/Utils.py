import math
from Matriz import Matriz

# Función para calcular la cantidad de información
# p: probabilidad del evento
# r: base del logaritmo (default 2)
# retorna la cantidad de información en bits (si r=2)
def cantidadInformacion(p: float, r=2) -> float:
    if p <= 0 or p > 1:
        resultado = 0
    else:
        resultado = math.log(1/p, r)
    return resultado

# Funcion para calcular entropia
# probabilidades: lista de probabilidades de los eventos
# r: base del logaritmo (default 2)
# retorna la entropia en bits (si r=2)
def entropia(probabilidades: list, r=2) -> float:
    H = 0
    for p in probabilidades:
        H += p * cantidadInformacion(p, r)
    return H

# Funcion que devuelve alfabeto con sus probabilidades
def getAlfaProbabilidades(texto: str):
    alfabeto = []
    probabilidades = []
    longitud = len(texto)
    for simbolo in texto:
        if simbolo in alfabeto:
            index = alfabeto.index(simbolo)
            probabilidades[index] += 1
        else:
            alfabeto.append(simbolo)
            probabilidades.append(1)
    for i in range(len(probabilidades)):
        probabilidades[i] /= longitud
    return alfabeto, probabilidades

# Función que, a partir de una matriz de transición, devuelve la matriz de estados estables
def estadosEstables(matriz: Matriz[float]) -> Matriz[float]:
    if matriz.cantFilas != matriz.cantColumnas:
        raise ValueError("La matriz debe ser cuadrada para calcular los estados estables.")
    
    n = matriz.cantFilas
    A = [[0.0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i == j:
                A[i][j] = matriz.get(i, j) - 1.0
            else:
                A[i][j] = matriz.get(i, j)

    for j in range(n):
        A[n-1][j] = 1.0
    
    b = [0.0 for _ in range(n)]
    b[n-1] = 1.0
    
    A_matriz = Matriz(n, n, A)
    b_matriz = Matriz(n, 1, [[b[i]] for i in range(n)])
    
    A_inv = A_matriz.inversa
    estados = A_inv * b_matriz
    
    return estados