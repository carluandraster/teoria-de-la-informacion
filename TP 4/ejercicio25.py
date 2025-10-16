from ejercicio24 import es_correcto

MENSAJE_A = bytearray([int("00100001", 2),
                       int("10000111", 2),
                       int("10000010", 2),
                       int("10100110", 2),
                       int("10000010", 2)])

MENSAJE_B = bytearray([int("00101101", 2),
                       int("10011001", 2),
                       int("10001010", 2),
                       int("10011100", 2),
                       int("10000010", 2)])

MENSAJE_C = bytearray([int("00101010", 2),
                       int("10000010", 2),
                       int("10011010", 2),
                       int("10011111", 2),
                       int("10100101", 2)])

MENSAJE_D = bytearray([int("00010100", 2),
                       int("10010000", 2),
                       int("10011110", 2),
                       int("10011001", 2),
                       int("10000010", 2)])

MENSAJE_E = bytearray([int("00110101", 2),
                       int("10011010", 2),
                       int("10101011", 2),
                       int("10100100", 2),
                       int("10000010", 2)])

MENSAJE_F = bytearray([int("00001001", 2),
                       int("10101001", 2),
                       int("10100101", 2),
                       int("10001011", 2),
                       int("10100110", 2)])

MENSAJE_G = bytearray([int("00011101", 2),
                       int("10010011", 2),
                       int("10011101", 2),
                       int("10001100", 2),
                       int("10011111", 2)])

MENSAJE_H = bytearray([int("00111110", 2),
                       int("10000111", 2),
                       int("10010000", 2),
                       int("10000010", 2),
                       int("10101010", 2)])

def mensaje_correcto(mensaje: bytearray) -> bool:
    """Dado un mensaje recibido, verifica si es correcto.
    
    :param mensaje: bytearray que representa el mensaje recibido.
    
    :return: True si el mensaje es correcto, False en caso contrario.
    """
    is_mensaje_correcto = True
    i = 0
    while i < len(mensaje) and is_mensaje_correcto:
        byte = mensaje[i]
        if not es_correcto(byte):
            is_mensaje_correcto = False
        i += 1

    return is_mensaje_correcto

def corregir_mensaje(mensaje: bytearray) -> bytearray | None:
    """Dado un mensaje recibido, intenta corregirlo si es posible.
    
    :param mensaje: bytearray que representa el mensaje recibido.
    
    :return: un bytearray con el mensaje corregido o None si no se pudo corregir.
    """

    if mensaje_correcto(mensaje):
        return mensaje
    else:
        i = 0
        j = 0
        while i < len(mensaje) and not mensaje_correcto(mensaje):
            while j < 8 and not mensaje_correcto(mensaje):
                mensaje[i] ^= 1 << j
                if mensaje_correcto(mensaje):
                    return mensaje
                else:
                    j += 1
            i += 1
            j = 0
            mensaje[i] ^= 1 << j
    
    return None
    