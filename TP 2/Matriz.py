from typing import TypeVar, Generic

T = TypeVar('T')

# Implementación de la clase Matriz genérica
class Matriz(Generic[T]):
    __cantFilas: int
    __cantColumnas: int
    __matriz: list[list[T]]

    def __init__(self, filas: int, columnas: int, valores: list[list[T]]) -> None:
        self.__cantFilas = filas
        self.__cantColumnas = columnas
        self.__matriz = [[valores[i][j] if i < len(valores) and j < len(valores[i]) else None for j in range(columnas)] for i in range(filas)]

    @property
    def cantidadFilas(self) -> int:
        return self.__cantFilas
    @property
    def cantidadColumnas(self) -> int:
        return self.__cantColumnas

    def get(self, fila: int, columna: int) -> T | None:
        if 0 <= fila < self.__cantFilas and 0 <= columna < self.__cantColumnas:
            return self.__matriz[fila][columna]
        return None
    
    def set(self, fila: int, columna: int, valor: T) -> None:
        if 0 <= fila < self.__cantFilas and 0 <= columna < self.__cantColumnas:
            self.__matriz[fila][columna] = valor
    
    def __eq__(self, value):
        if not isinstance(value, Matriz):
            return NotImplemented
        return (self.__cantFilas, self.__cantColumnas, self.__matriz) == (value.__cantFilas, value.__cantColumnas, value.__matriz)

    def __ne__(self, otro: 'Matriz[T]') -> bool:
        return not self == otro
    
    def __add__(self, other: 'Matriz[T]') -> 'Matriz[T]':
        if self.__cantFilas != other.__cantFilas or self.__cantColumnas != other.__cantColumnas:
            raise ValueError("Las matrices deben tener las mismas dimensiones para sumarse.")
        
        resultado = [[self.__matriz[i][j] + other.__matriz[i][j] for j in range(self.__cantColumnas)] for i in range(self.__cantFilas)]
        return Matriz(self.__cantFilas, self.__cantColumnas, resultado)
    
    def __iadd__(self, other: 'Matriz[T]') -> 'Matriz[T]':
        if self.__cantFilas != other.__cantFilas or self.__cantColumnas != other.__cantColumnas:
            raise ValueError("Las matrices deben tener las mismas dimensiones para sumarse.")
        
        for i in range(self.__cantFilas):
            for j in range(self.__cantColumnas):
                self.__matriz[i][j] += other.__matriz[i][j]
        return self
    
    def __sub__(self, other: 'Matriz[T]') -> 'Matriz[T]':
        if self.__cantFilas != other.__cantFilas or self.__cantColumnas != other.__cantColumnas:
            raise ValueError("Las matrices deben tener las mismas dimensiones para restarse.")
        
        resultado = [[self.__matriz[i][j] - other.__matriz[i][j] for j in range(self.__cantColumnas)] for i in range(self.__cantFilas)]
        return Matriz(self.__cantFilas, self.__cantColumnas, resultado)
    
    def __isub__(self, other: 'Matriz[T]') -> 'Matriz[T]':
        if self.__cantFilas != other.__cantFilas or self.__cantColumnas != other.__cantColumnas:
            raise ValueError("Las matrices deben tener las mismas dimensiones para restarse.")
        
        for i in range(self.__cantFilas):
            for j in range(self.__cantColumnas):
                self.__matriz[i][j] -= other.__matriz[i][j]
        return self
    
    def __mul__(self, other) -> 'Matriz[T]':
        if isinstance(other, Matriz):
            # Multiplicación de matrices
            if self.__cantColumnas != other.__cantFilas:
                raise ValueError("El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz para multiplicarse.")
            resultado = [[sum(self.__matriz[i][k] * other.__matriz[k][j] for k in range(self.__cantColumnas)) for j in range(other.__cantColumnas)] for i in range(self.__cantFilas)]
            return Matriz(self.__cantFilas, other.__cantColumnas, resultado)
        else:
            # Multiplicación por escalar
            resultado = [[self.__matriz[i][j] * other for j in range(self.__cantColumnas)] for i in range(self.__cantFilas)]
            return Matriz(self.__cantFilas, self.__cantColumnas, resultado)
    
    def __imul__(self, otro) -> 'Matriz[T]':
        self = self * otro
        return self

    def __str__(self) -> str:
        return '\n'.join(['\t'.join([str(self.__matriz[i][j]) if self.__matriz[i][j] is not None else 'None' for j in range(self.__cantColumnas)]) for i in range(self.__cantFilas)])
    
    def __repr__(self) -> str:
        return f"Matriz(filas={self.__cantFilas}, columnas={self.__cantColumnas}, valores={self.__matriz})"
    
    @property
    def inversa(self) -> 'Matriz[T]':
        if self.__cantFilas != self.__cantColumnas:
            raise ValueError("La matriz debe ser cuadrada para calcular su inversa.")
        
        n = self.__cantFilas
        identidad = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        matriz_extendida = [self.__matriz[i] + identidad[i] for i in range(n)]
        
        for i in range(n):
            if matriz_extendida[i][i] == 0:
                for j in range(i + 1, n):
                    if matriz_extendida[j][i] != 0:
                        matriz_extendida[i], matriz_extendida[j] = matriz_extendida[j], matriz_extendida[i]
                        break
            
            divisor = matriz_extendida[i][i]
            if divisor == 0:
                raise ValueError("La matriz no es invertible.")
            
            for j in range(2 * n):
                matriz_extendida[i][j] /= divisor
            
            for k in range(n):
                if k != i:
                    factor = matriz_extendida[k][i]
                    for j in range(2 * n):
                        matriz_extendida[k][j] -= factor * matriz_extendida[i][j]
        
        inversa = [fila[n:] for fila in matriz_extendida]
        return Matriz(n, n, inversa)
    
    def getFila(self, fila: int) -> list[T]:
        if 0 <= fila < self.__cantFilas:
            return self.__matriz[fila]
        raise IndexError("Índice de fila fuera de rango.")
    
    def getColumna(self, columna: int) -> list[T]:
        if 0 <= columna < self.__cantColumnas:
            return [self.__matriz[i][columna] for i in range(self.__cantFilas)]
        raise IndexError("Índice de columna fuera de rango.")