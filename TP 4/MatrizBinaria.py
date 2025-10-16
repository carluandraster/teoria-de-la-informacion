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
        if len(lista) > 8:
            for i, bit in enumerate(lista):
                if bit:
                    byte |= (1 << (7 - i % 8))
                if i % 8 == 7:
                    vector_de_bytes.append(byte)
                    byte = 0
            if len(lista) % 8 != 0:
                vector_de_bytes.append(byte)
        else:
            for i, bit in enumerate(lista):
                if bit:
                    byte |= (1 << (len(lista) - 1 - i))
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
    
    def get_errores(self) -> list[tuple]:
        """Devuelve una lista de tuplas que representan las posiciones de los errores.
        
        :return: Una lista de tuplas (fila, columna) indicando las posiciones de los errores.
        Si un error en columna no está apareado con un error en fila, la fila será -1 y viceversa.
        """
        errores_en_columnas = []
        errores_en_filas = []
        
        # Recorrer columnas
        for i in range(self.cantidad_columnas):
            columna = self.getColumna(i)
            columna_str = ''.join([bin(byte) for byte in columna])
            if columna_str[1:].count('1') % 2 != columna[0] & 0x80:
                errores_en_columnas.append(i)

        # Recorrer filas
        for i in range(self.cantidad_filas):
            fila = self.getFila(i)
            fila_str = ''.join([bin(byte) for byte in fila])
            if fila_str[:-1].count('1') % 2 != fila[-1] & 0x1:
                errores_en_filas.append(i)

        # Emparejar errores
        errores = []
        for i, (columna, fila) in enumerate(zip(errores_en_columnas, errores_en_filas)):
            errores.append((fila, columna))
        if len(errores_en_columnas) > len(errores_en_filas):
            for columna in errores_en_columnas[len(errores_en_filas):]:
                errores.append((-1, columna))
        elif len(errores_en_filas) > len(errores_en_columnas):
            for fila in errores_en_filas[len(errores_en_columnas):]:
                errores.append((fila, -1))

        return errores
    
    def corregir(self) -> bool:
        """Intenta corregir los errores en la matriz si es posible.
        
        :return: True si se pudieron corregir los errores, False en caso contrario.
        """
        errores = self.get_errores()
        if len(errores) == 0:
            return True
        if len(errores) > 1:
            return False
        
        fila, columna = errores[0]

        self[fila][columna] = not self[fila][columna]

        return True
    
    def __str__(self):
        string = ""
        for fila in range(self.cantidad_filas):
            string += " ".join(str(bit) for bit in self.getFila(fila)) + "\n"
        return string