def get_frecuencias(texto: str)-> dict:
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