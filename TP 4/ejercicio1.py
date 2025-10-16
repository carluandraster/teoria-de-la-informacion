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
    entropia = entropia_de_la_fuente(palabras_codigo, probabilidades)
    print(f"Entropía: {entropia:.2f}, Longitud media: {longitud_media_n:.2f}")
    return entropia <= longitud_media_n/n and longitud_media_n/n <= entropia + 1/n