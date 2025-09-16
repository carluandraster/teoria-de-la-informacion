import math

def get_alfbeto_codigo(C: list[str])->str:
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
    x = ""
    for codigo in C:
        for caracter in codigo:
            if caracter not in x:
                x += caracter
    return x

def get_longitudes(codigos: list[str])->list[int]:
    """
    Dada una lista con palabras código, obtiene una lista con las longitudes de cada palabra código.

    Parámetros:
        - codigos: list[str] - Lista de palabras código.
    
    Retorna:
        - list[int] - Lista con las longitudes de cada palabra código.
    
    Contrato:
        - Precondición: codigos debe ser una lista de cadenas no vacías y distinta de None.
        - Postcondición: El resultado es una lista de enteros donde cada entero representa la longitud de la palabra código correspondiente en la lista de entrada.
    """
    return [len(codigo) for codigo in codigos]

def sumatoria_de_kraft(C: list[str])->float:
    """"
    Dada una lista que contiene las palabras código de una codificación, calcula la sumatoria de la inecuación de Kraft.

    Parámetros:
        - C: list[str] - Lista de palabras código.
    
    Retorna: (float) valor de la sumatoria de la inecuación de Kraft.
    
    Contrato:
        - Precondición: C debe ser una lista de cadenas no vacías y distinta de None.
        - Postcondición: El resultado es un número flotante que representa la sumatoria de la inecuación de Kraft para las palabras código proporcionadas.
    """
    r = len(C)
    L = get_longitudes(C)
    sumatoria = 0
    for l_i in L:
        sumatoria += r ** -l_i
    return sumatoria