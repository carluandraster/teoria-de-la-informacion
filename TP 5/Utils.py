def get_frecuencias(texto: str)-> dict[str, int]:
    """
    Esta función recibe un texto y devuelve un diccionario con la frecuencia de cada carácter en el texto.
    
    :param texto: El texto del cual se quieren obtener las frecuencias de los caracteres.
    :return: Un diccionario donde las claves son los caracteres y los valores son sus frecuencias.
    """
    frecuencias = {}
    for char in texto:
        if char in frecuencias:
            frecuencias[char] += 1
        else:
            frecuencias[char] = 1
    return frecuencias

def get_frecuencias_relativas(texto: str) -> dict[str, float]:
    """
    Esta función recibe un texto y devuelve un diccionario con la frecuencia relativa de cada carácter en el texto.
    
    :param texto: El texto del cual se quieren obtener las frecuencias relativas de los caracteres.
    :return: Un diccionario donde las claves son los caracteres y los valores son sus frecuencias relativas.
    """
    frecuencias = get_frecuencias(texto)
    total_caracteres = len(texto)
    frecuencias_relativas = {char: freq / total_caracteres for char, freq in frecuencias.items()}
    return frecuencias_relativas