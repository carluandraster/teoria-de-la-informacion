from ejercicio24 import from_caracter_to_byte
from MatrizBinaria import MatrizBinaria as mb

def generar_bytearray(x: str) -> bytearray:
    """Dada una cadena de caracteres, genera una secuencia de bytes (bytearray) que
    contiene su representación con código ASCII y sus bits de paridad vertical,
    longitudinal y cruzada.

    :param x: cadena de caracteres a convertir.
    
    :return: bytearray que representa la cadena con sus bits de paridad.
"""
    byte = 0
    vector_de_bytes = bytearray()
    vector_de_bytes.append(0)
    for caracter in x:
        byte = from_caracter_to_byte(caracter)
        vector_de_bytes.append(byte)
        vector_de_bytes[0] ^= byte
    return vector_de_bytes

def get_mensaje_original(x: bytearray) -> str:
    """Dada una secuencia de bytes, devuelve el mensaje original o una cadena de caracteres vacía
    si no se pueden corregir los errores.

    :param x: bytearray que representa la cadena con sus bits de paridad.
    
    :return: cadena de caracteres original.
    """
    matriz = mb([format(byte, '08b') for byte in x])
    exito = matriz.corregir()
    if exito:
        mensaje = ''.join(chr(matriz.getFila(i)[0] >> 1 & 0x7f) for i in range(1, matriz.cantidad_filas))
        return mensaje
    else:
        return ''