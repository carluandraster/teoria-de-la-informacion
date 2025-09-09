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

def esUnivocamenteDecodificable(codigo: set) -> bool:
    """
    Verifica si un código es unívocamente decodificable.

    Parámetros:
        - codigo (set): Lista de cadenas que representan el código.
    Retorna:
        - bool: True si el código es unívocamente decodificable, False en caso contrario.
    Precondiciones:
        - codigo no está vacío.
        - codigo es distinto de None
        - el codigo es no singular
    """
    S = [codigo, set()]
    i = 0
    seguir = True
    while seguir:
        for x in S[0]:
            for y in S[i]:
                if x.startswith(y) and x != y:
                    S[i].add(x[len(y):])
        if codigo.intersection(S[i]) != set(): # Si la intersección no es vacía, no es unívocamente decodificable
            respuesta = False
            seguir = False
        else:
            j = 0
            while j <= i and S[j] != S[i]:
                j += 1
            if S[i] == set() or S[i] == S[j]:
                respuesta = True
                seguir = False
            else:
                S.append(set())
                i += 1
    return respuesta

def seleccionar(codigo: set) -> str:
    """
    Clasifica un codigo como instantáneo, unívocamente decodificable o no unívocamente decodificable.

    Parámetros:
        - codigo (set): Lista de cadenas que representan el código.
    Retorna:
        - str: "instantáneo", "unívocamente decodificable" o "no unívocamente decodificable"
    Precondiciones:
        - codigo no está vacío.
        - codigo es distinto de None
        - el codigo es no singular
    """
    if esInstantaneo(list(codigo)):
        return "instantáneo"
    elif esUnivocamenteDecodificable(codigo):
        return "unívocamente decodificable"
    else:
        return "no unívocamente decodificable"

CODIGO_1 = {"010", "101", "000", "111"}
CODIGO_2 = {"111", "000", "11", "00"}

print("Codigo 1 es ", seleccionar(CODIGO_1))
print("Codigo 2 es ", seleccionar(CODIGO_2))