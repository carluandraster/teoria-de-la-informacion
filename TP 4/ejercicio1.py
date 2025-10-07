from Utils import generarConExtension, entropia_de_la_fuente, get_longitud_media

def primer_teorema_shannon(probabilidades: list[float], palabras_codigo: list[str], n: int) -> bool:
    """
    Verifica el primer teorema de Shannon para una fuente de información.

    Parámetros:
        - probabilidades (list[float]): lista de probabilidades de cada símbolo en la fuente.
        - palabras_codigo (list[str]): lista de palabras del código asociado a la fuente.
        - n (int): longitud fija de las palabras del código.

    Retorna: true si se cumple el teorema, false en caso contrario.
    """
    s_n, probabilidades_n = generarConExtension(palabras_codigo, probabilidades, n)
    longitud_media_n = get_longitud_media(s_n, probabilidades_n)
    print("L = ", longitud_media_n)
    entropia_n = entropia_de_la_fuente(s_n, probabilidades_n)
    print("H = ", entropia_n)
    return entropia_n <= longitud_media_n and longitud_media_n <= entropia_n + 1