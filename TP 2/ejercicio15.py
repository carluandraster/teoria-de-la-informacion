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

def simularMensaje(alfabeto: list[str], transiciones: Matriz[float], longitud: int, simbolo_inicial: str = None) -> str:
    """
    Simula un mensaje emitido por una fuente de primer orden.
    
    Parámetros:
        alfabeto (list[str]): El alfabeto de la fuente.
        transiciones (Matriz[float]): La matriz de transiciones de primer orden.
        longitud (int): La longitud del mensaje a simular.
        simbolo_inicial (str, opcional): El símbolo inicial del mensaje. Si no se proporciona, se selecciona aleatoriamente.
    Precondiciones:
        - El alfabeto no debe estar vacío.
        - La matriz de transiciones debe estar normalizada.
    Retorna:
        str: El mensaje simulado.
    """
    if not alfabeto:
        raise ValueError("El alfabeto no debe estar vacío.")
    if not transiciones:
        raise ValueError("La matriz de transiciones no debe estar vacía.")

    mensaje = ""
    if simbolo_inicial is None:
        simbolo_inicial = random.choice(alfabeto)
    mensaje += simbolo_inicial

    for _ in range(longitud - 1):
        simbolo_actual = mensaje[-1]
        fila = alfabeto.index(simbolo_actual)
        siguiente_simbolo = random.choices(alfabeto, weights=transiciones[fila])[0]
        mensaje += siguiente_simbolo

    return mensaje