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

def corregir_mensaje(mensaje: bytearray) -> bytearray | None:
    """Dado un mensaje recibido, intenta corregirlo si es posible.
    
    :param mensaje: bytearray que representa el mensaje recibido.
    
    :return: un bytearray con el mensaje corregido o None si no se pudo corregir.
    """

    problema_solucionado = True
    primer_error_encontrado = False
    segundo_error_encontrado = False
    index = 0
    while index < len(mensaje) and not segundo_error_encontrado and problema_solucionado:
        if not es_correcto(mensaje[index]):
            if primer_error_encontrado:
                segundo_error_encontrado = True
            else:
                i = 0
                problema_solucionado = False
                while i < 8 and not problema_solucionado:
                    acum = 0
                    for b in mensaje[1:]:
                        acum += b >> (7 - i) & 0b00000001
                    if acum % 2 != (mensaje[0] >> (7 - i) & 0b00000001):
                        mensaje[index + 1] ^= (1 << (7 - i))
                        problema_solucionado = True
                    i += 1
                primer_error_encontrado = True
        index += 1
    return mensaje if problema_solucionado and not segundo_error_encontrado else None

def from_bytes_to_string(mensaje: bytearray) -> str:
    """Convierte un mensaje en bytes a su representación en string.
    
    :param mensaje: bytearray que representa el mensaje recibido.
    
    :return: una cadena de caracteres con la representación del mensaje.
    """
    resultado = ""
    for byte in mensaje[1:]:
        resultado += chr(byte >> 1 & 0x7f)
    
    return resultado

if __name__ == "__main__":
    mensaje_corregido = corregir_mensaje(MENSAJE_A)
    if mensaje_corregido is None:
        print("No se pudo corregir el mensaje A.")
    else:
        print("Mensaje A:", from_bytes_to_string(mensaje_corregido))
    mensaje_corregido = corregir_mensaje(MENSAJE_B)
    if mensaje_corregido is None:
        print("No se pudo corregir el mensaje B.")
    else:
        print("Mensaje B:", from_bytes_to_string(mensaje_corregido))

    mensaje_corregido = corregir_mensaje(MENSAJE_C)
    if mensaje_corregido is None:
        print("No se pudo corregir el mensaje C.")
    else:
        print("Mensaje C:", from_bytes_to_string(mensaje_corregido))

    mensaje_corregido = corregir_mensaje(MENSAJE_D)
    if mensaje_corregido is None:
        print("No se pudo corregir el mensaje D.")
    else:
        print("Mensaje D:", from_bytes_to_string(mensaje_corregido))

    mensaje_corregido = corregir_mensaje(MENSAJE_E)
    if mensaje_corregido is None:
        print("No se pudo corregir el mensaje E.")
    else:
        print("Mensaje E:", from_bytes_to_string(mensaje_corregido))

    mensaje_corregido = corregir_mensaje(MENSAJE_F)
    if mensaje_corregido is None:
        print("No se pudo corregir el mensaje F.")
    else:
        print("Mensaje F:", from_bytes_to_string(mensaje_corregido))

    mensaje_corregido = corregir_mensaje(MENSAJE_G)
    if mensaje_corregido is None:
        print("No se pudo corregir el mensaje G.")
    else:
        print("Mensaje G:", from_bytes_to_string(mensaje_corregido))

    mensaje_corregido = corregir_mensaje(MENSAJE_H)
    if mensaje_corregido is None:
        print("No se pudo corregir el mensaje H.")
    else:
        print("Mensaje H:", from_bytes_to_string(mensaje_corregido))