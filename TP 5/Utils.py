def getAlfaProbabilidades(texto: str):
    """
    Dada una cadena de caracteres, devuelve una lista con su alfabeto y una lista con sus probabilidades.
    
    Parámetros:
        texto (str): La cadena de caracteres.
    Retorna:
        tuple: Una tupla que contiene una lista con el alfabeto y una lista con sus probabilidades.
    """
    alfabeto = []
    probabilidades = []
    longitud = len(texto)
    for simbolo in texto:
        if simbolo in alfabeto:
            index = alfabeto.index(simbolo)
            probabilidades[index] += 1
        else:
            alfabeto.append(simbolo)
            probabilidades.append(1)
    for i in range(len(probabilidades)):
        probabilidades[i] /= longitud
    return alfabeto, probabilidades

def get_alfaprobabilidades_ordenado(texto: str):
    """
    Dada una cadena de caracteres, devuelve una lista con su alfabeto ordenado y una lista con sus probabilidades, ambas ordenadas alfabéticamente.
    
    Parámetros:
        texto (str): La cadena de caracteres.
    """
    alfabeto, probabilidades = getAlfaProbabilidades(texto)
    indices_ordenados = sorted(range(len(alfabeto)), key=lambda i: alfabeto[i])
    alfabeto_ordenado = [alfabeto[i] for i in indices_ordenados]
    probabilidades_ordenadas = [probabilidades[i] for i in indices_ordenados]
    return alfabeto_ordenado, probabilidades_ordenadas