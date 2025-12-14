import math
from math import log2
from Canal import Canal
from Matriz import Matriz

def cantidadInformacion(p: float, r: int=2) -> float:
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

def entropia(probabilidades: list[float], r: int=2) -> float:
    """Calcula la entropía de una lista de probabilidades.

    Parámetros:
        probabilidades (list[float]): lista de probabilidades de los eventos.
        r (int): base del logaritmo (default 2).
    
    Retorna:
        float: la entropía en bits (si r=2).
    """
    h: float = 0.0
    for p in probabilidades:
        h += p * cantidadInformacion(p, r)
    return h

def funcion_entropia(omega: float, r: int=2) -> float:
    """Calcula la función de entropía para una probabilidad omega.

    Parámetros:
        omega (float): probabilidad del evento (0 < omega <= 1).
        r (int): base del logaritmo (default 2).
    
    Retorna:
        float: el valor de la función de entropía en bits (si r=2).
    """
    if omega <= 0 or omega > 1:
        resultado = 0
    else:
        resultado = entropia([omega, 1 - omega], r)
    return resultado

def get_frecuencias(texto: str)-> dict[str, int]:
    """
    Esta función recibe un texto y devuelve un diccionario con la frecuencia de cada carácter en el texto.
    
    :param str texto: El texto del cual se quieren obtener las frecuencias de los caracteres.
    :return dict[str, int]: Un diccionario donde las claves son los caracteres y los valores son sus frecuencias.
    """
    frecuencias: dict[str, int] = {}
    for char in texto:
        if char in frecuencias:
            frecuencias[char] += 1
        else:
            frecuencias[char] = 1
    return frecuencias

def get_frecuencias_relativas(texto: str) -> dict[str, float]:
    """
    Esta función recibe un texto y devuelve un diccionario con la frecuencia relativa de cada carácter en el texto.
    
    :param str texto: El texto del cual se quieren obtener las frecuencias relativas de los caracteres.
    :return dict[str, float]: Un diccionario donde las claves son los caracteres y los valores son sus frecuencias relativas.
    """
    frecuencias = get_frecuencias(texto)
    total_caracteres = len(texto)
    frecuencias_relativas = {char: freq / total_caracteres for char, freq in frecuencias.items()}
    return frecuencias_relativas

def es_uniforme(matriz: Matriz[float]) -> bool:
    """Determina si un canal es uniforme.

    Un canal es uniforme si todas las filas de su matriz contienen los mismos números.

    Parámetros:
    -----------
    matriz : Matriz
        Matriz de transición del canal.

    Retorna:
    --------
    bool
        True si el canal es uniforme, False en caso contrario.
    """
    primera_fila = matriz[0]
    for i in range(1, matriz.cantidadFilas):
        for j in range(matriz.cantidadColumnas):
            if matriz[i][j] not in primera_fila:
                return False
    return True

def es_canal_sin_ruido(matriz_canal: Matriz[float]) -> bool:
    """
    Devuelve true si la matriz corresponde a un canal sin ruido, es decir, si cada columna tiene un único valor distinto de 0.

    Parámetros:
    ------------------
    - matriz_canal (Matriz[float]): Matriz que representa el canal de comunicación.

    Retorna:
    -----------------
    - bool: True si el canal es sin ruido, False en caso contrario.
    """
    N = matriz_canal.cantidadFilas
    M = matriz_canal.cantidadColumnas
    j = 0
    respuesta = True
    while j<M and respuesta:
        contador_valores_distintos_de_cero = 0
        i = 0
        while i<N and contador_valores_distintos_de_cero <= 1:
            if matriz_canal[i][j] != 0:
                contador_valores_distintos_de_cero += 1
            i += 1
        if contador_valores_distintos_de_cero > 1:
            respuesta = False
        j += 1
    return respuesta

def es_canal_determinante(matriz_canal: Matriz[float]) -> bool:
    """Devuelve true si la matriz corresponde a un canal determinante, es decir, si cada fila tiene un único valor distinto de 0.
    
    Parámetros:
    ------------------
    - matriz_canal (Matriz[float]): Matriz que representa el canal de comunicación.
    
    Retorna:
    -----------------
    - bool: True si el canal es determinante, False en caso contrario.
    """
    N = matriz_canal.cantidadFilas
    M = matriz_canal.cantidadColumnas
    i = 0
    respuesta = True
    while i<N and respuesta:
        contador_valores_distintos_de_cero = 0
        j = 0
        while j<M and contador_valores_distintos_de_cero <= 1:
            if matriz_canal[i][j] != 0:
                contador_valores_distintos_de_cero += 1
            j += 1
        if contador_valores_distintos_de_cero != 1:
            respuesta = False
        i += 1
    return respuesta

def _get_cantidad_columnas_no_nulas(matriz: Matriz[float]) -> int:
    """
    Devuelve la cantidad de columnas no nulas en una matriz.

    Parámetros:
    -----------
    matriz : Matriz
        Matriz de transición del canal.

    Retorna:
    --------
    int
        Cantidad de columnas no nulas.
    """
    cant_col_no_nulas = 0
    for j in range(matriz.cantidadColumnas):
        columna = matriz.getColumna(j)
        if any(p > 0 for p in columna):
            cant_col_no_nulas += 1
    return cant_col_no_nulas

def es_canal_bsc(matriz: Matriz[float]) -> bool:
    """
    Determina si un canal es un Binary Symmetric Channel (BSC).

    Un canal es un BSC si tiene dos símbolos de entrada y dos símbolos de salida,
    y las probabilidades de error son iguales para ambos símbolos.

    Parámetros:
    -----------
    matriz : Matriz
        Matriz de transición del canal.

    Retorna:
    --------
    bool
        True si el canal es un BSC, False en caso contrario.
    """
    if matriz.cantidadFilas != 2 or _get_cantidad_columnas_no_nulas(matriz) != 2:
        return False
    p_error_0 = matriz[0][1]
    p_error_1 = matriz[1][0]
    return math.isclose(p_error_0, p_error_1)

def capacidad_canal(matriz: Matriz[float]) -> float:
    """
    Determina la capacidad de un canal de comunicación.

    La capacidad de un canal es la máxima cantidad de información que puede ser transmitida.

    Parámetros:
    -----------
    matriz : Matriz
        Matriz de transición del canal.

    Retorna:
    --------
    float
        Capacidad del canal.
    """
    if es_canal_determinante(matriz):
        cant_col_no_nulas = _get_cantidad_columnas_no_nulas(matriz)
        return log2(cant_col_no_nulas)
    else:
        if es_canal_sin_ruido(matriz):
            return log2(matriz.cantidadFilas)
        if es_uniforme(matriz):
            return log2(_get_cantidad_columnas_no_nulas(matriz)) - entropia(matriz[0])
        else:
            if es_canal_bsc(matriz):
                p_error = matriz[0][1]
                return 1 - funcion_entropia(p_error)
            else:
                if matriz.cantidadFilas == 2:
                    _, capacidad = maximizar_informacion_mutua(matriz)
                    return capacidad
                else:
                    raise ValueError("Cálculo de capacidad no implementado para este tipo de canal.")

def maximizar_informacion_mutua(canal: Matriz[float], h: float = 0.0001) -> tuple[float, float]:
    """
    Calcula la capacidad de un canal binario y la probabilidad óptima de entrada

    Args:
        canal (Matriz[float]): Matriz de transición del canal binario.
        h (float): Paso.
    
    Returns:
        tuple[float, float]: probabilidad óptima de entrada y capacidad del canal.
    """
    capacidad = -1.0
    omega = 0.0
    probabilidad_optima = 0.0
    while omega <= 1.0:
        p_apriori = [omega, 1 - omega]
        canal_obj = Canal(canal, p_apriori)
        info_mutua = canal_obj.get_informacion_mutua()
        if info_mutua > capacidad:
            capacidad = info_mutua
            probabilidad_optima = omega
        omega += h
    return probabilidad_optima, capacidad