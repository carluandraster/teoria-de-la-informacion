import math
import random
from Matriz import Matriz
from typing import List, Tuple
import MatrizFactory as mf

def cantidadInformacion(p: float, r=2) -> float:
    """
    Calcula la cantidad de información de un evento dado su probabilidad.
    
    Parámetros:
        p (float): La probabilidad del evento (0 < p <= 1).
        r (int): La base del logaritmo (default 2).
    Retorna:
        float: La cantidad de información en bits.
    """
    if p <= 0 or p > 1:
        resultado = 0
    else:
        resultado = math.log(1/p, r)
    return resultado

def get_informaciones(probabilidades: list, r=2) -> list:
    """
    Dada una lista de probabilidades, devuelve una lista con las cantidades de información correspondientes.

    Parámetros:
        - probabilidades (list): Lista de probabilidades de los eventos.
        - r (int): Base del logaritmo (default 2).
    
    Retorna: list(float): Lista de cantidades de información correspondientes a las probabilidades dadas.

    Contrato:
        - probabilidades != None
        - len(probabilidades) > 0
        - sum(probabilidades) == 1
        - r > 1
    """
    return [cantidadInformacion(p, r) for p in probabilidades]

def entropia(probabilidades: list, r=2) -> float:
    """
    Calcula la entropía de una fuente de información dada una lista de probabilidades.
    
    Parámetros:
        probabilidades (list): Lista de probabilidades de los eventos.
        r (int): Base del logaritmo (default 2).
    Retorna:
        float: La entropía en la unidad que corresponda (por defecto, en bits).
    """
    H = 0
    for p in probabilidades:
        H += p * cantidadInformacion(p, r)
    return H

def getAlfaProbabilidades(texto: str) -> Tuple[List[str], List[float]]:
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

def monte_carlo(alfabeto: list, probabilidades_acumuladas: list, n: int) -> list:
    """
    Genera una simulación de Monte Carlo basada en un alfabeto y sus probabilidades acumuladas.

    Parámetros:
        - alfabeto (list): Lista de símbolos del alfabeto.
        - probabilidades_acumuladas (list): Lista de probabilidades acumuladas correspondientes a los símbolos del alfabeto.
        - n (int): Número de símbolos a generar en la simulación.
    
    Retorna: lista de símbolos generados en la simulación.

    Contrato:
        - alfabeto es una lista no vacía de símbolos y es distinta de None.
        - probabilidades_acumuladas es una lista no vacía de números en el rango [0, 1] y es distinta de None.
        - n es un entero positivo y es distinto de None.
        - len(alfabeto) == len(probabilidades_acumuladas)
        - probabilidades_acumuladas está ordenada en forma no decreciente.
        - La lista que se retorna solo tiene símbolos que están en alfabeto.
    """
    simulacion = []
    for _ in range(n):
        r = random.random()
        for i, p_acum in enumerate(probabilidades_acumuladas):
            if r <= p_acum:
                simulacion.append(alfabeto[i])
                break
    return simulacion

def entropiaBinaria(omega: float) -> float:
    """
    Calcula la entropía de una fuente binaria de memoria nula.
    
    Parámetros:
        - omega (float): probabilidad del símbolo 0
    
    Retorna: (float) entropía de la fuente binaria

    Contrato:
        - 0 <= omega <= 1
    """
    return entropia([omega, 1 - omega])

# Función auxiliar para la función generarConExtension
def generar_combinaciones(alfabeto: list, N: int) -> list:
    """Genera todas las combinaciones posibles de longitud N
    a partir del alfabeto dado.
    
    Parametros:
        alfabeto (list): lista de elementos del alfabeto
        N (int): longitud de las combinaciones a generar
    Retorna:
        list: lista de combinaciones generadas
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
        alfabeto (list): lista de elementos del alfabeto
        probabilidades (list[float]): lista de probabilidades de cada elemento del alfabeto
        N (int): orden de la extensión
    Retorna:
        tuple: (nuevas_letras, nuevas_probabilidades)
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

def estadosEstables(matriz: Matriz[float]) -> Matriz[float]:
    """
    Calcula la matriz de estados estables de una cadena de Markov dada su matriz de transición.
    
    Parámetros:
        matriz (Matriz[float]): La matriz de transición de la cadena de Markov.
    Retorna:
        Matriz[float]: La matriz de estados estables.
    Lanza:
        ValueError: Si la matriz no es cuadrada.
    """
    if matriz.cantidadFilas != matriz.cantidadColumnas:
        raise ValueError("La matriz debe ser cuadrada para calcular los estados estables.")

    n = matriz.cantidadFilas
    A = matriz - mf.identidad(n)

    for j in range(n):
        A[n-1][j] = 1.0

    b = mf.ceros(n, 1)
    b[n-1][0] = 1.0

    return A.inversa * b

def entropiaMarkoviana(matriz: Matriz[float]) -> float:
    """
    Calcula la entropía markoviana de una cadena de Markov dada su matriz de transición.
    
    Parámetros:
        matriz (Matriz[float]): La matriz de transición de la cadena de Markov.
    Retorna:
        float: La entropía markoviana.
    Lanza:
        ValueError: Si la matriz no es cuadrada.
    """
    if matriz.cantidadFilas != matriz.cantidadColumnas:
        raise ValueError("La matriz debe ser cuadrada para calcular la entropía markoviana.")
    estados = estadosEstables(matriz)
    h = 0
    for i in range(matriz.cantidadColumnas):
        columna = matriz.getColumna(i)
        h += estados[i][0] * entropia(columna)
    return h

def obtenerAlfabetoYTransiciones(mensaje: str) -> tuple[list[str], Matriz[float]]:
    """
    Obtiene el alfabeto y la matriz de transiciones de primer orden de un mensaje.
    
    Parámetros:
        mensaje (str): El mensaje emitido por la fuente.
    Precondiciones:
        - El mensaje no debe estar vacío.
        - El mensaje debe ser representativo de la fuente
    Retorna:
        tuple: Una tupla que contiene una lista con el alfabeto y una lista con su matriz de transiciones.
    """
    alfabeto = []
    longitud = len(mensaje)

    # Obtener alfabeto
    for simbolo in mensaje:
        if simbolo not in alfabeto:
            alfabeto.append(simbolo)

    transiciones = mf.ceros(len(alfabeto), len(alfabeto))

    # Obtener matriz de transiciones
    for i in range(longitud - 1):
        transiciones[alfabeto.index(mensaje[i+1])][alfabeto.index(mensaje[i])] += 1

    transiciones.normalizar()

    return alfabeto, transiciones

def simularMensaje(alfabeto: list[str], transiciones: Matriz[float], longitud: int, simbolo_inicial: str = "") -> str:
    """
    Simula un mensaje emitido por una fuente de primer orden.
    
    Parámetros:
        alfabeto (list[str]): El alfabeto de la fuente.
        transiciones (Matriz[float]): La matriz de transiciones de primer orden.
        longitud (int): La longitud del mensaje a simular.
        simbolo_inicial (str, opcional): El símbolo inicial del mensaje. Si no se proporciona, se selecciona aleatoriamente.
    Precondiciones:
        - El alfabeto no debe estar vacío.
        - El mensaje no debe estar vacío.
        - La matriz de transiciones no debe estar vacía.
        - La matriz de transiciones debe estar normalizada.
    Retorna:
        str: El mensaje simulado.
    """

    mensaje = ""
    if simbolo_inicial == "":
        simbolo_inicial = random.choice(alfabeto)
    mensaje += simbolo_inicial

    for _ in range(longitud - 1):
        simbolo_actual = mensaje[-1]
        columna = alfabeto.index(simbolo_actual)
        siguiente_simbolo = random.choices(alfabeto, weights=transiciones.getColumna(columna))[0]
        mensaje += siguiente_simbolo

    return mensaje

def esFuenteDeMemoriaNula(matriz_de_transiciones: Matriz[float], tolerancia: float = 0.1) -> bool:
    """
    Verifica si una fuente es de memoria nula.
    
    Parámetros:
        matriz_de_transiciones (Matriz[float]): La matriz de transiciones de la fuente.
        tolerancia (float): Un valor de tolerancia para considerar que una probabilidad es cero.
    Retorna:
        bool: True si la fuente es de memoria nula, False en caso contrario.
    """
    for fila in matriz_de_transiciones:
        if max(fila)-min(fila) > tolerancia:
            return False
    return True