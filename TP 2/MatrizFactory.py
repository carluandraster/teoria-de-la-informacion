from Matriz import Matriz
import random

def ceros(filas: int, columnas: int) -> Matriz[float]:
    return Matriz(filas, columnas, [[0.0 for _ in range(columnas)] for _ in range(filas)])

def unos(filas: int, columnas: int) -> Matriz[float]:
    return Matriz(filas, columnas, [[1.0 for _ in range(columnas)] for _ in range(filas)])

def relleno(filas: int, columnas: int, valor: float) -> Matriz[float]:
    return Matriz(filas, columnas, [[valor for _ in range(columnas)] for _ in range(filas)])

def identidad(tamano: int) -> Matriz[float]:
    return Matriz(tamano, tamano, [[1.0 if i == j else 0.0 for j in range(tamano)] for i in range(tamano)])

def aleatorios(filas: int, columnas: int, min_val: float = 0.0, max_val: float = 1.0) -> Matriz[float]:
    return Matriz(filas, columnas, [[random.uniform(min_val, max_val) for _ in range(columnas)] for _ in range(filas)])