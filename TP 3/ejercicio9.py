import math

def get_cadena_caracteres(codigos: list[str])->str:
    """
    Dada una lista que contiene las palabras código de una codificación, obtiene una cadena de caracteres con el alfabeto código.

    Parámetros:
        - codigos: list[str] - Lista de palabras código.

    Retorna:
        - str - Cadena de caracteres con el alfabeto código.
    
    Contrato:
        - Precondición: codigos debe ser una lista de cadenas no vacías y distina de None.
        - Postcondición: El resultado es una cadena que contiene todos los caracteres únicos presentes en las palabras código.
    """
    n = math.floor(math.random()*25)
    resultado = ""
    for i in range(n):
        resultado += codigos[math.floor(math.random()*len(codigos))]
    return resultado

def get_longitudes(codigos: list[str])->str:
    return [len(codigo) for codigo in codigos]