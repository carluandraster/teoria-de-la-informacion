import math
import random
import Unidad2 as u2

# Constantes
INSTANTANEO = "instantáneo"
UNIVOCO = "unívoco"
NO_SINGULAR = "no singular"
BLOQUE = "bloque"

# Funciones

def esNoSingular(codigos: list) -> bool:
    """
    Determina si un codigo de encriptación es no singular; es decir, que no se repitan palabras codigo

    Parametros:
        - codigos (list): Lista de códigos.
    Retorna:
        - bool: True si el código es no singular, False en caso contrario.
    Precondiciones:
        - codigos no está vacía.
        - codigos es distinto de None.
    """
    codigos_vistos = set()
    for codigo in codigos:
        if codigo in codigos_vistos:
            return False
        codigos_vistos.add(codigo)
    return True

def esInstantaneo(codigo: list) -> bool:
    """
    Verifica si un código es instantáneo.

    Parámetros:
        - codigo (list): Lista de cadenas que representan el código.
    Retorna:
        - bool: True si el código es instantáneo, False en caso contrario.
    Precondiciones:
        - codigo no está vacío.
        - codigo es distinto de None
    """
    for i in range(len(codigo)):
        for j in range(len(codigo)):
            if i != j and codigo[i].startswith(codigo[j]):
                return False
    return True

def esUnivocamenteDecodificable(codigo: list) -> bool:
    """
    Verifica si un código es unívocamente decodificable.

    Parámetros:
        - codigo (list): Lista de cadenas que representan el código.
    Retorna:
        - bool: True si el código es unívocamente decodificable, False en caso contrario.
    Precondiciones:
        - codigo no está vacío.
        - codigo es distinto de None
    """
    S = [set(codigo), set()]
    i = 0
    seguir = True
    while seguir:
        for x in S[0]:
            for y in S[i]:
                if x.startswith(y) and x != y:
                    S[i+1].add(x[len(y):])
                else:
                    if y.startswith(x) and x != y:
                        S[i+1].add(y[len(x):])
        if S[0].intersection(S[i+1]) != set(): # Si la intersección no es vacía, no es unívocamente decodificable
            respuesta = False
            seguir = False
        else:
            if S[i+1] == set() or S[i+1] in S[0:i+1]:
                respuesta = True
                seguir = False
            else:
                S.append(set())
                i += 1
    return respuesta

def clasificar(codigo: list) -> str:
    """
    Clasifica un código

    Parámetros:
        - codigo: list
            Lista de cadenas que representan el código a clasificar.
    
    Retorna:
        - str
            Una cadena que indica si el código es "bloque", "instantáneo", "unívoco" o "no singular"
    
    Contrato:
        - El parámetro 'codigo' debe ser una lista de cadenas no vacías.
        - La función retorna una cadena que indica la clasificación del código.
    """
    if esNoSingular(codigo):
        if esInstantaneo(codigo):
            return INSTANTANEO
        else:
            if esUnivocamenteDecodificable(codigo):
                return UNIVOCO
            else:
                return NO_SINGULAR
    else:
        return BLOQUE
    
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
    r = len(get_alfabeto_codigo(C))
    L = get_longitudes(C)
    sumatoria = 0.0
    for l_i in L:
        sumatoria += r ** -l_i
    return sumatoria

def entropia_de_la_fuente(codigos: list[str], probabilidades: list[float])->float:
    """
    Calcula la entropía de una fuente de información dada su distribución de probabilidades y su abecedario.

    Parámetros:
        - probabilidades (list[float]): Lista de probabilidades de los símbolos de la fuente.
        - codigos (list[str]): Lista de palabras código.
    
    Retorna: un float que representa la entropía de la fuente.
    
    Contrato:
        - sum(probabilidades) == 1
        - all(p >= 0 and p<=1 for p in probabilidades)
        - r > 1 (base del logaritmo)
        - len(probabilidades) > 0
        - len(codigos) > 0
    """
    return u2.entropia(probabilidades, len(get_alfabeto_codigo(codigos)))

def get_longitud_media(palabras_codigo: list[str], probabilidades: list[float])->float:
    """
    Dada 2 listas, una de palabras código y otra de probabilidades, devuelve la longitud media del código.

    Parámetros:
        - palabras_codigo (list[str]): Lista de palabras código.
        - probabilidades (list[float]): Lista de probabilidades de los símbolos de la fuente.
    
    Retorna: un float que representa la longitud media del código.

    Contrato:
        - len(palabras_codigo) == len(probabilidades)
        - sum(probabilidades) == 1
        - all(p >= 0 and p<=1 for p in probabilidades)
    """
    longitudes = get_longitudes(palabras_codigo)
    longitud_media = 0
    for p_i, l_i in zip(probabilidades, longitudes):
        longitud_media += p_i * l_i
    return longitud_media

def get_longitudes_maximas(probabilidades: list[float], r: int) -> list[int]:
    """Calculas las longitudes máximas que debe tener un código para ser compacto
    
    Parametros:
        - probabilidades: lista de probabilidades de los símbolos
        - r: base del código (2 para binario, 3 para ternario, etc.)
    
    Retorna: lista de longitudes máximas para cada símbolo
    
    Contrato:
        - probabilidades es distinta de None y no es una lista vacía
        - todos los elementos de probabilidades son mayores que 0 y menores o iguales que 1
        - la suma de los elementos de probabilidades es igual a 1
        - Se devuelve una lista de enteros positivos
        - r es un entero mayor que 1
    """
    longitudes = []
    for p in probabilidades:
        l = math.ceil(-math.log(p, r))
        longitudes.append(l)
    return longitudes

def es_codigo_compacto(codigos: list[str], probabilidades: list[float]) -> bool:
    """
    Determina si un conjunto de códigos es compacto.

    Un conjunto de códigos es compacto si cada longitud de código es menor o igual
    que la función techo del logaritmo en base r (donde r es el tamaño del alfabeto) de
    la inversa a la probabilidad asociada a ese código.

    Parámetros:
        codigos (list[str]): Lista de códigos.
        probabilidades (list[float]): Lista de probabilidades asociadas a cada código.

    Retorna:
        bool: True si el conjunto de códigos es compacto, False en caso contrario.
        
    Contrato:
        - codigos es distinto de None y de lista vacía
        - probabilidades es distinto de None y de lista vacía
        - len(codigos) == len(probabilidades)
        - todas las probabilidades son mayores que 0 y menores o iguales a 1
        - la suma de todas las probabilidades es igual a 1
    """
    if esInstantaneo(codigos):
        R = len(get_alfabeto_codigo(codigos))
        LONGITUDES = get_longitudes(codigos)
        i = 0
        respuesta = True
        while i < len(codigos) and respuesta:
            limite_superior = math.ceil(-math.log(probabilidades[i], R))
            if LONGITUDES[i] > limite_superior:
                respuesta = False
            i += 1
    else:
        respuesta = False
    return respuesta

def simular_fuente(codigos: list[str], probabilidades: list[float], n: int) -> list[str]:
    """
    Simula la salida de una fuente de información discreta.

    Parameteros:
        - codigos: lista de símbolos del código.
        - probabilidades: lista de probabilidades asociadas a cada símbolo.
        - n: cantidad de símbolos a simular.
    
    Retorna: (list[str]) lista de símbolos simulados.

    Contrato:
        - len(codigos) > 0
        - len(probabilidades) > 0
        - len(codigos) == len(probabilidades)
        - sum(probabilidades) == 1
        - all(p >= 0 and p <= 1 for p in probabilidades)
        - n > 0
    """
    simulacion = []
    for _ in range(n):
        simulacion.append(random.choices(codigos, weights=probabilidades)[0])
    return simulacion