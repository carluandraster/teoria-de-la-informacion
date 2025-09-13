import ejercicio6 as ej6

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
            return "instantáneo"
        else:
            if ej6.esUnivocamenteDecodificable(codigo):
                return "unívoco"
            else:
                return "no singular"
    else:
        return "bloque"