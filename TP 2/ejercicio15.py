from Matriz import Matriz

# Dada una cadena de caracteres que representa un mensaje emitido por una fuente,
# devuelve una lista con su alfabeto y su matriz de transiciones de primer orden.
def obtenerAlfabetoYTransiciones(mensaje: str) -> tuple[list[str], Matriz[float]]:
    alfabeto = []
    longitud = len(mensaje)

    # Obtener alfabeto
    for simbolo in mensaje:
        if simbolo not in alfabeto:
            alfabeto.append(simbolo)

    transiciones = Matriz(len(alfabeto), 0, [])

    # Obtener matriz de transiciones
    for i in range(longitud - 1):
        columna = [0] * len(alfabeto)
        columna[alfabeto.index(mensaje[i + 1])] += 1
        transiciones.agregarColumna(columna)

    # Normalizar matriz de transiciones
    for i in range(len(transiciones)):
        total = sum(transiciones[i])
        if total > 0:
            transiciones[i] = [x / total for x in transiciones[i]]

    return alfabeto, Matriz(len(transiciones), len(transiciones[0]), transiciones)

# Test
print(obtenerAlfabetoYTransiciones("Hola")[1])