from Matriz import Matriz
from typing import TypeVar, Generic, List, Optional

def ceros(filas: int, columnas: int) -> Matriz[float]:
    return Matriz(filas, columnas, [[0.0 for _ in range(columnas)] for _ in range(filas)])

def identidad(tamano: int) -> Matriz[float]:
    return Matriz(tamano, tamano, [[1.0 if i == j else 0.0 for j in range(tamano)] for i in range(tamano)])
