from Matriz import Matriz

class MatrizBinaria(Matriz[bool]):
    """Clase que representa una matriz binaria (de valores booleanos).
    La primera fila y la última columna son bits de paridad.
    
    :extends Matriz[bool]: Clase base Matriz parametrizada con booleanos."""
    
    def __init__(self, binarios: list[str]):
        super().__init__(self._convertir_a_matriz(binarios))

    def _convertir_a_matriz(self, binarios: list[str]) -> list[list[bool]]:
        return [[c == '1' for c in fila] for fila in binarios]
    
    def _convertir_a_bytearray(self, lista: list[bool]) -> bytearray:
        byte = 0
        vector_de_bytes = bytearray()
        for i, bit in enumerate(lista):
            if bit:
                byte |= (1 << (7 - i % 8))
            if i % 8 == 7:
                vector_de_bytes.append(byte)
                byte = 0
        if len(lista) % 8 != 0:
            vector_de_bytes.append(byte)
        return vector_de_bytes
    
    def getColumna(self, columna: int) -> bytearray:
        return self._convertir_a_bytearray(super().getColumna(columna))

    def getFila(self, fila: int) -> bytearray:
        return self._convertir_a_bytearray(super().getFila(fila))
    
    def get_distancia_de_hamming(self) -> int:
        """Calcula la distancia de Hamming mínima entre las filas de la matriz,
        excluyendo la fila de paridad.
        
        :return: La distancia de Hamming mínima entre las filas."""
        min_distancia = float('inf')
        for i in range(1, self.cantidad_filas - 1):
            for j in range(i + 1, self.cantidad_filas - 1):
                fila_i = self.getFila(i)
                fila_j = self.getFila(j)
                distancia = 0
                for k in range(min(len(fila_i), len(fila_j))):
                    distancia += bin(fila_i[k] ^ fila_j[k]).count('1')
                if distancia < min_distancia:
                    min_distancia = distancia
        return min_distancia if min_distancia != float('inf') else 0
    
    def get_errores_detectables(self) -> int:
        """Calcula la cantidad máxima de errores detectables por la matriz.
        
        :return: La cantidad máxima de errores detectables."""
        d = self.get_distancia_de_hamming()
        return d - 1 if d > 0 else 0
    
    def get_errores_corregibles(self) -> int:
        """Calcula la cantidad máxima de errores corregibles por la matriz.

        :return: La cantidad máxima de errores corregibles."""
        d = self.get_distancia_de_hamming()
        return (d - 1) // 2 if d > 0 else 0
    