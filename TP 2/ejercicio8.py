import Utils

# Calcula la entropía de una fuente binaria de memoria nula
def entropiaBinaria(omega: float) -> float:
    if omega < 0 or omega > 1:
        raise ValueError("La probabilidad debe estar en el rango [0, 1]")
    return Utils.entropia([omega, 1 - omega])