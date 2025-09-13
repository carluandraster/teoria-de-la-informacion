import ejercicio6 as ej6

# Constantes
INSTANTANEO = "instantáneo"
UNIVOCO = "unívoco"
NO_SINGULAR = "no singular"
BLOQUE = "bloque"

def clasificar(codigo: list) -> str:
    """
    Clasifica un código

    Parámetros:
        - codigo: list
            Lista de cadenas que representan el código a clasificar.
    
    Retorna:
        - str
            Una cadena que indica si el código es "bloque", "instantáneo", "unívoco" o "no singular"
    
    Contrato:
        - El parámetro 'codigo' debe ser una lista de cadenas no vacías.
        - La función retorna una cadena que indica la clasificación del código.
    """
    if ej6.esNoSingular(codigo):
        if ej6.esInstantaneo(codigo):
            return INSTANTANEO
        else:
            if ej6.esUnivocamenteDecodificable(codigo):
                return UNIVOCO
            else:
                return NO_SINGULAR
    else:
        return BLOQUE