"""Módulo que contiene la implementación de una clase Matriz genérica en Python."""

from typing import TypeVar, Generic

T = TypeVar('T')

# Implementación de la clase Matriz genérica
class Matriz(Generic[T]):
    """
    Clase que representa una matriz genérica.
    
    Métodos:
    -------------
    - <b>__init__(self, valores: list[list[T]]):</b> Constructor de la clase Matriz.
    - <b>cantidadFilas(self) -> int:</b> Devuelve la cantidad de filas de la matriz.
    - <b>cantidadColumnas(self) -> int:</b> Devuelve la cantidad de columnas de la matriz.
    - <b>inversa(self) -> 'Matriz[float]':</b> Devuelve la matriz inversa si es posible.
    - <b>traspuesta(self) -> 'Matriz[T]':</b> Devuelve la matriz transpuesta.
    - <b>normalizarColumnas(self) -> None:</b> Normaliza las columnas de la matriz.
    
    También soporta las siguientes operaciones:
    -------------
    - Acceso y modificación de elementos mediante índices.
    - Comparación de matrices (==, !=).
    - Suma y resta de matrices (+, -, +=, -=).
    - Multiplicación de matrices y por escalares (*, *=).
    - Representación en cadena (__str__, __repr__).
    """
    __cantFilas: int
    __cantColumnas: int
    __matriz: list[list[T]]

    def __init__(self, valores: list[list[T]]):
        """
        Constructor de la clase Matriz.

        Parámetros:
            - valores (list[list[T]]): Una lista de listas que representa los valores iniciales de la matriz.
        
        Contrato:
            - len(valores) > 0
            - all(len(fila) == len(valores[0]) for fila in valores)
            - Contruye una matriz con las dimensiones dadas y llena con los valores proporcionados.
        """
        self.__cantFilas = len(valores)
        self.__cantColumnas = len(valores[0])
        self.__matriz = [[valores[i][j] if i < len(valores) and j < len(valores[i]) else None for j in range(self.__cantColumnas)] for i in range(self.__cantFilas)]

    @property
    def cantidadFilas(self) -> int:
        return self.__cantFilas
    @property
    def cantidadColumnas(self) -> int:
        return self.__cantColumnas

    def __getitem__(self, indice: int):
        return self.__matriz[indice]
    
    def __setitem__(self, key: int, value: T):
        self.__matriz[key] = value
    
    def __eq__(self, value: 'Matriz[T]') -> bool:
        return (self.__cantFilas, self.__cantColumnas, self.__matriz) == (value.__cantFilas, value.__cantColumnas, value.__matriz)

    def __ne__(self, otro: 'Matriz[T]') -> bool:
        return not self == otro
    
    def __add__(self, other: 'Matriz[T]') -> 'Matriz[T]':
        if self.__cantFilas != other.__cantFilas or self.__cantColumnas != other.__cantColumnas:
            raise ValueError("Las matrices deben tener las mismas dimensiones para sumarse.")
        
        resultado = [[self.__matriz[i][j] + other.__matriz[i][j] for j in range(self.__cantColumnas)] for i in range(self.__cantFilas)]
        return Matriz(resultado)
    
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
        return Matriz(resultado)
    
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
            return Matriz(resultado)
        else:
            # Multiplicación por escalar
            resultado = [[self.__matriz[i][j] * other for j in range(self.__cantColumnas)] for i in range(self.__cantFilas)]
            return Matriz(resultado)
    
    def __imul__(self, otro) -> 'Matriz[T]':
        self = self * otro
        return self

    def __str__(self) -> str:
        return '\n'.join(['\t'.join([str(self.__matriz[i][j]) if self.__matriz[i][j] is not None else 'None' for j in range(self.__cantColumnas)]) for i in range(self.__cantFilas)])
    
    def __repr__(self) -> str:
        return f"Matriz(filas={self.__cantFilas}, columnas={self.__cantColumnas}, valores={self.__matriz})"
    
    @property
    def inversa(self) -> 'Matriz[T]':
        """
        Calcula la matriz inversa utilizando el método de eliminación de Gauss-Jordan.

        Retorna:
            Matriz[T]: La matriz inversa si es invertible.
        
        Lanza:
            ValueError: Si la matriz no es cuadrada o no es invertible.
        """
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
        return Matriz(inversa)
    
    def getFila(self, fila: int) -> list[T]:
        """
        Devuelve la fila especificada de la matriz.
        Parámetros:
            fila (int): El índice de la fila a obtener (0-indexado).
        Lanza:
            IndexError: Si el índice de fila está fuera de rango.
        """
        if 0 <= fila < self.__cantFilas:
            return self.__matriz[fila]
        raise IndexError("Índice de fila fuera de rango.")
    
    def getColumna(self, columna: int) -> list[T]:
        """
        Devuelve la columna especificada de la matriz.
        Parámetros:
            columna (int): El índice de la columna a obtener (0-indexado).
        Lanza:
            IndexError: Si el índice de columna está fuera de rango.
        """
        if 0 <= columna < self.__cantColumnas:
            return [self.__matriz[i][columna] for i in range(self.__cantFilas)]
        raise IndexError("Índice de columna fuera de rango.")
    
    def __len__(self) -> int:
        return self.__cantFilas * self.__cantColumnas
    
    def agregarFila(self, fila: list[T]) -> None:
        """
        Agrega una nueva fila a la matriz.

        Parámetros:
            fila (list[T]): La fila a agregar. Debe tener el mismo número de columnas que la matriz.

        Lanza:
            ValueError: Si la longitud de la fila no coincide con el número de columnas.
        """
        if len(fila) != self.__cantColumnas:
            raise ValueError("La fila debe tener el mismo número de columnas que la matriz.")
        self.__matriz.append(fila)
        self.__cantFilas += 1
    
    def agregarColumna(self, columna: list[T]) -> None:
        """
        Agrega una nueva columna a la matriz.

        Parámetros:
            columna (list[T]): La columna a agregar. Debe tener el mismo número de filas que la matriz.

        Lanza:
            ValueError: Si la longitud de la columna no coincide con el número de filas.
        """
        if len(columna) != self.__cantFilas:
            raise ValueError("La columna debe tener el mismo número de filas que la matriz.")
        for i in range(self.__cantFilas):
            self.__matriz[i].append(columna[i])
        self.__cantColumnas += 1

    def normalizar(self, axis = False) -> None:
        """
        Normaliza la matriz a lo largo del eje especificado.
        Parámetros:
            axis (bool): Si es True, normaliza por filas. Si es False, normaliza por columnas.
        """
        if axis:
            for i in range(self.__cantFilas):
                total = sum(self.__matriz[i])
                if total > 0:
                    self.__matriz[i] = [x / total for x in self.__matriz[i]]
        else:
            for j in range(self.__cantColumnas):
                total = sum(self.__matriz[i][j] for i in range(self.__cantFilas))
                if total > 0:
                    for i in range(self.__cantFilas):
                        self.__matriz[i][j] /= total
    
    @property
    def traspuesta(self) -> 'Matriz[T]':
        """
        Devuelve la matriz transpuesta.
        Retorna:
            Matriz[T]: La matriz transpuesta.
        """
        resultado = [[self.__matriz[j][i] for j in range(self.__cantFilas)] for i in range(self.__cantColumnas)]
        return Matriz(resultado)