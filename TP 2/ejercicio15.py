from Matriz import Matriz
import MatrizFactory as mf
import random

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