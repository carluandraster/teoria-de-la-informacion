def get_tasa_de_compresion(mensaje: str, mensaje_comprimido: bytearray) -> float:
    """
    Calcula la tasa de compresión entre un mensaje original y su versión comprimida.

    Args:
        mensaje (str): El mensaje original.
        mensaje_comprimido (bytearray): El mensaje comprimido.

    Returns:
        float: La tasa de compresión, definida como la división entre el tamaño original y el tamaño comprimido.
    """
    tamanio_mensaje = len(mensaje)
    tamanio_mensaje_comprimido = len(mensaje_comprimido)
    tasa_de_compresion = tamanio_mensaje / tamanio_mensaje_comprimido if tamanio_mensaje_comprimido else 0
    return tasa_de_compresion