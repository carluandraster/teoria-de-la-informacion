"""Factory de matrices con diferentes inicializaciones.

Funciones:
---------------
- <b>ceros(filas: int, columnas: int) -> Matriz[float]:</b> Crea una matriz de ceros con las dimensiones especificadas.
- <b>unos(filas: int, columnas: int) -> Matriz[float]:</b> Crea una matriz de unos con las dimensiones especificadas.
- <b>relleno(filas: int, columnas: int, valor: float) -> Matriz[float]:</b> Crea una matriz rellenada con el valor especificado.
- <b>identidad(tamano: int) -> Matriz[int]:</b> Crea una matriz identidad de tamaño especificado.
- <b>aleatorios(filas: int, columnas: int, min_val: float = 0.0, max_val: float = 1.0) -> Matriz[float]:</b> Crea una matriz de números aleatorios con las dimensiones especificadas.
"""


from .Matriz import Matriz
import random

def ceros(filas: int, columnas: int) -> Matriz[float]:
    """
    Crea una matriz de ceros con las dimensiones especificadas.
    
    Parámetros:
        filas (int): Número de filas de la matriz.
        columnas (int): Número de columnas de la matriz.
    Retorna:
        Matriz[float]: Una matriz de ceros con las dimensiones dadas.
    """
    return Matriz([[0.0 for _ in range(columnas)] for _ in range(filas)])

def unos(filas: int, columnas: int) -> Matriz[float]:
    """
    Crea una matriz de unos con las dimensiones especificadas.
    
    Parámetros:
        filas (int): Número de filas de la matriz.
        columnas (int): Número de columnas de la matriz.
    Retorna:
        Matriz[float]: Una matriz de unos con las dimensiones dadas.
    """
    return Matriz([[1.0 for _ in range(columnas)] for _ in range(filas)])

def relleno(filas: int, columnas: int, valor: float) -> Matriz[float]:
    """
    Crea una matriz rellenada con el valor especificado.

    Parámetros:
        filas (int): Número de filas de la matriz.
        columnas (int): Número de columnas de la matriz.
        valor (float): Valor con el que rellenar la matriz.
    Retorna:
        Matriz[float]: Una matriz rellenada con el valor especificado.
    """
    return Matriz([[valor for _ in range(columnas)] for _ in range(filas)])

def identidad(tamano: int) -> Matriz[int]:
    """
    Crea una matriz identidad de tamaño especificado.

    Parámetros:
        tamano (int): Tamaño de la matriz identidad.

    Retorna:
        Matriz[float]: Una matriz identidad de tamaño x tamano.
    """
    return Matriz([[1 if i == j else 0 for j in range(tamano)] for i in range(tamano)])

def aleatorios(filas: int, columnas: int, min_val: float = 0.0, max_val: float = 1.0) -> Matriz[float]:
    """
    Crea una matriz de números aleatorios con las dimensiones especificadas.

    Parámetros:
        filas (int): Número de filas de la matriz.
        columnas (int): Número de columnas de la matriz.
        min_val (float): Valor mínimo para los números aleatorios.
        max_val (float): Valor máximo para los números aleatorios.
    Retorna:
        Matriz[float]: Una matriz de números aleatorios con las dimensiones dadas.
    """
    return Matriz([[random.uniform(min_val, max_val) for _ in range(columnas)] for _ in range(filas)])