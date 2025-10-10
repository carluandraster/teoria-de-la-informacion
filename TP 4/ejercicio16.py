def get_tasa_de_compresion(mensaje: str, mensaje_comprimido: bytearray) -> float:
    """
    Calcula la tasa de compresión entre un mensaje original y su versión comprimida.

    Args:
        mensaje (str): El mensaje original.
        mensaje_comprimido (bytearray): El mensaje comprimido.

    Returns:
        float: La tasa de compresión, definida como la diferencia entre el tamaño del mensaje original
               y el tamaño del mensaje comprimido, dividido por el tamaño del mensaje original.
    """
    tamanio_mensaje = len(mensaje)
    tamanio_mensaje_comprimido = len(mensaje_comprimido)
    tasa_de_compresion = (tamanio_mensaje -  tamanio_mensaje_comprimido )/ tamanio_mensaje
    return tasa_de_compresion