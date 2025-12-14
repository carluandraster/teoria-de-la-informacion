from math import floor

def get_M(n: int, C: float, epsilon: float) -> int:
    """
    Calcula el número máximo de mensajes M que se pueden transmitir
    con una tasa de error menor o igual a epsilon, dado un canal
    con capacidad C y un bloque de longitud n.

    :param int n: Longitud del bloque.
    :param float C: Capacidad del canal en bits por símbolo.
    :param float epsilon: Tasa de error máxima permitida.

    :return int: Número máximo de mensajes M.
    """
    if epsilon <= 0 or epsilon >= C:
        raise ValueError("Epsilon debe estar en el rango (0, C).")

    # Cálculo de M usando la fórmula derivada del segundo teorema de Shannon
    M = 2 ** (n * (C- epsilon))

    return floor(M)