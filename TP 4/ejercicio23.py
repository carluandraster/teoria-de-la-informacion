from ejercicio22 import get_distancia_de_hamming

CODIGO_1 = ["0100100", "0101000", "0010010", "0100000"]
CODIGO_2 = ["0100100", "0010010", "0101000", "0100001"]
CODIGO_3 = ["0110000", "0000011", "0101101", "0100110"]

def resolver(nombre: str, codigo: list[str]) -> None:
    distancia, detectables, corregibles = get_distancia_de_hamming(codigo)
    print("---------",nombre, "---------")
    print("Distancia de Hamming:", distancia)
    print("Errores detectables:", detectables)
    print("Errores corregibles:", corregibles)
    print("\n")

resolver("CODIGO 1", CODIGO_1)
resolver("CODIGO 2", CODIGO_2)
resolver("CODIGO 3", CODIGO_3)