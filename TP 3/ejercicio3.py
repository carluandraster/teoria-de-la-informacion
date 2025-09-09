def esSingular(codigos: list) -> bool:
    """
    Determina si un codigo de encriptación es singular; es decir, si existen dos letras que se encripten de la misma manera.

    Parametros:
        - codigos (list): Lista de códigos.
    Retorna:
        - bool: True si el código es singular, False en caso contrario.
    Precondiciones:
        - codigos no está vacía.
        - codigos es distinto de None.
    """
    codigos_vistos = set()
    for codigo in codigos:
        if codigo in codigos_vistos:
            return True
        codigos_vistos.add(codigo)
    return False

# Ejemplo de uso
codigo1 = ["100", "10", "1000", "0"]
codigo2 = ["011", "0", "01", "011"]

if esSingular(codigo1):
    print("El código 1 es singular.")
else:
    print("El código 1 no es singular.")

if esSingular(codigo2):
    print("El código 2 es singular.")
else:
    print("El código 2 no es singular.")