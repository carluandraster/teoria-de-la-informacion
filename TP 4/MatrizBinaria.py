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