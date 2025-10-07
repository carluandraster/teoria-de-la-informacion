import math

def generar_combinaciones(alfabeto: list, N: int) -> list:
    """Genera todas las combinaciones posibles de longitud N
    a partir del alfabeto dado.
    
    Parámetros:
        alfabeto (list): lista de elementos del alfabeto.
        N (int): longitud de las combinaciones a generar.
    
    Retorna:
        list: lista de combinaciones generadas.
    """
    if N == 1:
        return [[letra] for letra in alfabeto]
    else:
        combinaciones_previas = generar_combinaciones(alfabeto, N - 1)
        nuevas_combinaciones = []
        for combinacion in combinaciones_previas:
            for letra in alfabeto:
                nuevas_combinaciones.append(combinacion + [letra])
        return nuevas_combinaciones

def generarConExtension(alfabeto: list, probabilidades: list[float], N: int):
    """Genera el alfabeto y la distribución de probabilidades
    de una fuente con extensión de orden N.
    
    Parámetros:
        alfabeto (list): lista de elementos del alfabeto.
        probabilidades (list[float]): lista de probabilidades de cada elemento del alfabeto.
        N (int): orden de la extensión.
    
    Retorna:
        tuple: (nuevas_letras, nuevas_probabilidades) donde nuevas_letras es una lista de combinaciones
        de longitud N y nuevas_probabilidades es una lista de probabilidades correspondientes.
    """
    if N <= 0:
        return [], []

    # Generar las combinaciones de longitud N
    combinaciones = generar_combinaciones(alfabeto, N)

    # Calcular las probabilidades de cada combinación
    nuevas_probabilidades = []
    for combinacion in combinaciones:
        probabilidad = 1.0
        for letra in combinacion:
            indice = alfabeto.index(letra)
            probabilidad *= probabilidades[indice]
        nuevas_probabilidades.append(probabilidad)

    # Convertir las combinaciones de listas de letras a cadenas
    nuevas_letras = [''.join(str(combinacion)) for combinacion in combinaciones]

    return nuevas_letras, nuevas_probabilidades

def cantidadInformacion(p: float, r=2) -> float:
    """Dada una probabilidad, calcula la cantidad de información.

    Parámetros:	
        p (float): probabilidad del evento (0 < p <= 1).
        r (int): base del logaritmo (default 2).
    
    Retorna:
        float: la cantidad de información en bits (si r=2).
    """
    if p <= 0 or p > 1:
        resultado = 0
    else:
        resultado = math.log(1/p, r)
    return resultado

def entropia(probabilidades: list, r=2) -> float:
    """Calcula la entropía de una lista de probabilidades.

    Parámetros:
        probabilidades (list): lista de probabilidades de los eventos.
        r (int): base del logaritmo (default 2).
    
    Retorna:
        float: la entropía en bits (si r=2).
    """
    H = 0
    for p in probabilidades:
        H += p * cantidadInformacion(p, r)
    return H

def get_alfabeto_codigo(C: list[str])->str:
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

def entropia_de_la_fuente(codigos: list[str], probabilidades: list[float]) -> float:
    """Calcula la entropía de una fuente de información dada su distribución de probabilidades y su abecedario.

    Parámetros:
        probabilidades (list[float]): Lista de probabilidades de los símbolos de la fuente.
        codigos (list[str]): Lista de palabras código.
    
    Retorna:
        float: un valor que representa la entropía de la fuente.
    
    Contrato:
        - sum(probabilidades) == 1
        - all(p >= 0 and p <= 1 for p in probabilidades)
        - r > 1 (base del logaritmo)
        - len(probabilidades) > 0
        - len(codigos) > 0
    """
    return entropia(probabilidades, len(get_alfabeto_codigo(codigos)))