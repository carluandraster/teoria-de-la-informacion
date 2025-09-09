import ejercicio6 as ej6

def clasificar(codigo: list) -> str:
    """
    Clasifica un código

    Parámetros:
        - codigo: list
            Lista de cadenas que representan el código a clasificar.
    Retorna:
        - str
            Una cadena que indica si el código es "bloque", "instantáneo", "unívoco" o "no singular".
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

codigo1  = ["011", "000", "010", "101", "001", "100"]
codigo2  = ["110", "100", "101", "001", "110", "010"]
codigo3  = ["10", "1100", "0101", "1011", "0", "110"]
codigo4  = ["1101", "10", "1111", "1100", "1110", "0"]
codigo5  = ["011", "0111", "01", "0", "011111", "01111"]
codigo6  = ["1110", "0", "110", "1101", "1011", "10"]

print("Código 1:",clasificar(codigo1))
print("Código 2:",clasificar(codigo2))
print("Código 3:",clasificar(codigo3))
print("Código 4:",clasificar(codigo4))
print("Código 5:",clasificar(codigo5))
print("Código 6:",clasificar(codigo6))