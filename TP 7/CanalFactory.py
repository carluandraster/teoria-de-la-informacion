"""Factory para crear objetos Canal a partir de secuencias de entrada y salida.

Funciones:
--------------
- <b>get_matriz_del_canal(entrada: str, salida: str) -> Matriz[float]:</b> Genera una matriz de canal a partir de las secuencias de entrada y salida.
- <b>crear_canal(entrada: str, salida: str) -> Canal:</b> Crea un objeto Canal a partir de las secuencias de entrada y salida."""

from .Canal import Canal
from .Matriz import Matriz
from . import MatrizFactory as mf
from .Utils import get_frecuencias_relativas

def get_matriz_del_canal(entrada: str, salida: str) -> Matriz[float]:
    """
    Genera una matriz de canal a partir de las secuencias de entrada y salida proporcionadas.

    :param entrada: Secuencia de símbolos de entrada.
    :param salida: Secuencia de símbolos de salida.

    :return: Matriz de canal donde cada elemento (i, j) representa la probabilidad
    """
    simbolos_entrada = sorted(set(entrada))
    simbolos_salida = sorted(set(salida))

    filas = len(simbolos_entrada)
    columnas = len(simbolos_salida)

    matriz_canal = mf.ceros(filas, columnas)

    for i, simbolo_entrada in enumerate(simbolos_entrada):
        total_simbolo_entrada = entrada.count(simbolo_entrada)
        for j, simbolo_salida in enumerate(simbolos_salida):
            conteo_conjunto = sum(
                1 for e, s in zip(entrada, salida) if e == simbolo_entrada and s == simbolo_salida
            )
            if total_simbolo_entrada > 0:
                matriz_canal[i][j] = conteo_conjunto / total_simbolo_entrada
            else:
                matriz_canal[i][j] = 0.0

    return matriz_canal

def crear_canal(entrada: str, salida: str) -> Canal:
    """
    Crea un objeto Canal a partir de las secuencias de entrada y salida proporcionadas.

    :param entrada: Secuencia de símbolos de entrada.
    :param salida: Secuencia de símbolos de salida.

    :return: Objeto Canal con la matriz de canal y las probabilidades a priori calculadas.
    """
    matriz_canal = get_matriz_del_canal(entrada, salida)
    simbolos_entrada = sorted(set(entrada))
    frecuencias_entrada = get_frecuencias_relativas(entrada)
    probabilidades_a_priori = [frecuencias_entrada[simbolo] for simbolo in simbolos_entrada]
    return Canal(matriz_canal, probabilidades_a_priori)