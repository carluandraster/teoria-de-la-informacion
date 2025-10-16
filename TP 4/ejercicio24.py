def from_caracter_to_byte(caracter: str) -> bytes:
    """
    Convierte un caracter a ASCII y al bit menos significativo lo usa para almacenar la paridad del código

    :param caracter: Caracter a convertir

    :return: Byte con el caracter y su bit de paridad
    """
    if len(caracter) != 1:
        raise ValueError("Input must be a single character.")
    ascii = bytes(caracter, 'ascii')
    return ascii[0] << 1 | (sum(bin(ascii[0])) % 2)

def es_correcto(byte: bytes) -> bool:
    """Dado un byte cuyo bit de paridad es el menos significativo, indica si el byte es correcto o no

    Args:
        byte (bytes): byte con la información y su bit de paridad

    Returns:
        bool: True si el byte es correcto, False en caso contrario
    """
    return sum(bin(byte[0] & 0b11111110)) % 2 == (byte[0] & 0b00000001)