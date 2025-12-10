def esNoSingular(codigos: list) -> bool:
    """
    Determina si un codigo de encriptación es no singular; es decir, que no se repitan palabras codigo

    Parametros:
        - codigos (list): Lista de códigos.
    Retorna:
        - bool: True si el código es no singular, False en caso contrario.
    Precondiciones:
        - codigos no está vacía.
        - codigos es distinto de None.
    """
    codigos_vistos = set()
    for codigo in codigos:
        if codigo in codigos_vistos:
            return False
        codigos_vistos.add(codigo)
    return True

def esInstantaneo(codigo: list) -> bool:
    """
    Verifica si un código es instantáneo.

    Parámetros:
        - codigo (list): Lista de cadenas que representan el código.
    Retorna:
        - bool: True si el código es instantáneo, False en caso contrario.
    Precondiciones:
        - codigo no está vacío.
        - codigo es distinto de None
    """
    for i in range(len(codigo)):
        for j in range(len(codigo)):
            if i != j and codigo[i].startswith(codigo[j]):
                return False
    return True

def esUnivocamenteDecodificable(codigo: list[str]) -> bool:
    """
    Verifica si un código es unívocamente decodificable.

    Parámetros:
        - codigo (list): Lista de cadenas que representan el código.
    Retorna:
        - bool: True si el código es unívocamente decodificable, False en caso contrario.
    Precondiciones:
        - codigo no está vacío.
        - codigo es distinto de None
    """
    S: list[set[str]] = [set(codigo), set()]
    i = 0
    seguir = True
    respuesta = True
    while seguir:
        for x in S[0]:
            for y in S[i]:
                if x.startswith(y) and x != y:
                    S[i+1].add(x[len(y):])
                else:
                    if y.startswith(x) and x != y:
                        S[i+1].add(y[len(x):])
        if S[0].intersection(S[i+1]) != set(): # Si la intersección no es vacía, no es unívocamente decodificable
            respuesta = False
            seguir = False
        else:
            if S[i+1] == set() or S[i+1] in S[0:i+1]:
                respuesta = True
                seguir = False
            else:
                S.append(set())
                i += 1
    return respuesta