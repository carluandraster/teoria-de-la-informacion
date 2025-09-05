import math
from Matriz import Matriz
import MatrizFactory as mf

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
        H += estados.get(i, 0) * entropia(columna)
    return H