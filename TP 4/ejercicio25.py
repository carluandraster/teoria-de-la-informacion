from MatrizBinaria import MatrizBinaria as mb

MENSAJE_A = mb(["00100001", "10000111", "10000010", "10100110", "10000010"])

MENSAJE_B = mb(["00101101", "10011001", "10001010", "10011100", "10000010"])

MENSAJE_C = mb(["00101010", "10000010", "10011010", "10011111", "10100101"]) 

MENSAJE_D = mb(["00010100", "10010000", "10011110", "10011001", "10000010"])

MENSAJE_E = mb(["00110101", "10011010", "10001010", "10011100", "10000010"])

MENSAJE_F = mb(["00001001", "10101001", "10100101", "10001011", "10100110"])

MENSAJE_G = mb(["00011101", "10010011", "10011101", "10001100", "10011111"])

MENSAJE_H = mb(["00111110", "10000111", "10010000", "10000010", "10101010"])


def from_mb_to_string(mensaje: mb) -> str:
    """Convierte un mensaje en bytes a su representación en string.
    
    :param mensaje: bytearray que representa el mensaje recibido.
    
    :return: una cadena de caracteres con la representación del mensaje.
    """
    resultado = ""
    for i in range(1, mensaje.cantidad_filas):
        byte = mensaje.getFila(i)[0]
        resultado += chr(byte >> 1 & 0x7f)

    return resultado

def resolver(nombre: str, mensaje: mb) -> None:
    """Intenta corregir el mensaje recibido e imprime el resultado.
    
    :param nombre: nombre del mensaje (A, B, C, ...).
    :param mensaje: bytearray que representa el mensaje recibido.
    """
    exito = mensaje.corregir()
    if not exito:
        print(f"No se pudo corregir el mensaje {nombre}.")
    else:
        print(f"Mensaje {nombre}: {from_mb_to_string(mensaje)}")

if __name__ == "__main__":
    resolver("A", MENSAJE_A)
    resolver("B", MENSAJE_B)
    resolver("C", MENSAJE_C)
    resolver("D", MENSAJE_D)
    resolver("E", MENSAJE_E)
    resolver("F", MENSAJE_F)
    resolver("G", MENSAJE_G)
    resolver("H", MENSAJE_H)