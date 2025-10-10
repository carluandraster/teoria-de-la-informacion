def comprimir_con_rlc(mensaje: str) -> bytearray:
    """Comprime un mensaje utilizando codificación por longitud de carrera (RLC).

    :param mensaje: El mensaje a comprimir.
    :return: El mensaje comprimido en formato bytearray, donde cada par de bytes representa (caracter, longitud).
    """
    if not mensaje:
        return bytearray()

    comprimido = bytearray()
    contador = 1
    caracter_anterior = mensaje[0]

    for caracter in mensaje[1:]:
        if caracter == caracter_anterior:
            contador += 1
        else:
            comprimido.append(ord(caracter_anterior))
            comprimido.append(contador)
            caracter_anterior = caracter
            contador = 1

    # Añadir el último grupo
    comprimido.append(ord(caracter_anterior))
    comprimido.append(contador)

    return comprimido