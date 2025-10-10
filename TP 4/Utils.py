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
    nuevas_letras = ["".join(combinacion) for combinacion in combinaciones]

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

def huffman(probabilidades: list[float]) -> list[str]:
    """
    Construye un codigo compacto de Huffman a partir de una lista de probabilidades.

    Parámetros:
        - probabilidades (list[float]): Lista de probabilidades de los símbolos de la fuente.
    
    Retorna: lista paralela a 'probabilidades' con las palabras código generadas.
    """

    items = [[p, [i]] for i, p in enumerate(probabilidades)]
    codigos = [''] * len(probabilidades)
    while len(items) > 1:
        items = sorted(items, key=lambda x: x[0])
        menor1 = items.pop(0)
        menor2 = items.pop(0)
        for i in menor1[1]:
            codigos[i] = '0' + codigos[i]
        for i in menor2[1]:
            codigos[i] = '1' + codigos[i]
        items.append([menor1[0] + menor2[0], menor1[1] + menor2[1]])
    return codigos

def _shannon_fano_rec(probabilidades: list[tuple[int, float]], codigos: list[str], prefijo=''):
    N = len(probabilidades)
    if N == 1:
        codigos[probabilidades[0][0]] = prefijo  # Corrección: usar el índice [0] no [1]
    else:
        total = sum(p for _, p in probabilidades)  # Corrección: usar _ para índice y p para probabilidad
        acumulado = 0
        i = 0
        while i < N and acumulado < total / 2:
            acumulado += probabilidades[i][1]
            i += 1
        if i > 0 and i < N:  # Corrección: agregar verificación de límites
            if total/2 - (acumulado - probabilidades[i - 1][1]) < acumulado - total/2:
                i -= 1
        # Corrección: verificar que las divisiones no sean vacías
        if i > 0:
            _shannon_fano_rec(probabilidades[:i], codigos, prefijo + '1')  # Corrección: usar i no i+1
        if i < N:
            _shannon_fano_rec(probabilidades[i:], codigos, prefijo + '0')  # Corrección: usar i no i+1

def shannon_fano(probabilidades: list[float]) -> list[str]:
    """
    Construye un codigo compacto de Shannon-Fano a partir de una lista de probabilidades.

    Parámetros:
        - probabilidades (list[float]): Lista de probabilidades de los símbolos de la fuente.
    
    Retorna: lista paralela a 'probabilidades' con las palabras código generadas.
    """
    indexed_probabilidades = list(enumerate(probabilidades))
    indexed_probabilidades.sort(key=lambda x: x[1], reverse=True)
    codigos = [''] * len(probabilidades)
    _shannon_fano_rec(indexed_probabilidades, codigos)
    return codigos

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