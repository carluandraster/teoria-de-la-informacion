from Utils import generarConExtension, entropia_de_la_fuente

def primer_teorema_shannon(probabilidades: list[float], palabras_codigo: list[str], n: int) -> bool:
    """
    Verifica el primer teorema de Shannon para una fuente de información.

    Parámetros:
        probabilidades (list[float]): lista de probabilidades de cada símbolo en la fuente.
        palabras_codigo (list[str]): lista de palabras del código asociado a la fuente.
        n (int): longitud fija de las palabras del código.

    Retorna: true si se cumple el teorema, false en caso contrario.
    """
    s_n, probabilidades_n = generarConExtension(palabras_codigo, probabilidades, n)