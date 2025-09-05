import Utils

def entropiaBinaria(omega: float) -> float:
    """Calcula la entropía de una fuente binaria de memoria nula.
    Parámetros:
        omega (float): probabilidad del símbolo 0
    Retorna:
        float: entropía de la fuente binaria
    """
    return Utils.entropia([omega, 1 - omega])