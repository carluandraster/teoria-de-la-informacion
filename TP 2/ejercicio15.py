from Matriz import Matriz
import MatrizFactory as mf

def obtenerAlfabetoYTransiciones(mensaje: str) -> tuple[list[str], Matriz[float]]:
    """
    Obtiene el alfabeto y la matriz de transiciones de primer orden de un mensaje.
    
    Parámetros:
        mensaje (str): El mensaje emitido por la fuente.
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

# Test
print(obtenerAlfabetoYTransiciones("Hola")[1])