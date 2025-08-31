import Utils

# Calcula la entropía de una fuente binaria de memoria nula
# Precondición: omega debe estar en el rango [0, 1]
def entropiaBinaria(omega: float) -> float:
    return Utils.entropia([omega, 1 - omega])