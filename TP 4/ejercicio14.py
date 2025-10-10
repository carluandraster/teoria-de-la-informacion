from ejercicio2 import codigo

FUENTE = [f"S{i}" for i in range(1, 5)]
MENSAJE_A = "ABACBAACABABAACBABA"
MENSAJE_B = "BACBAAABAAACBABACAB"
MENSAJE_C = "CBAABACBABAAACABABA"

def decodificar(mensaje_codificado: str) -> str:
    mensaje_decodificado = ""
    aux = ""
    for simbolo in mensaje_codificado:
        aux += simbolo
        if aux in codigo:
            mensaje_decodificado += FUENTE[codigo.index(aux)] + " " # El espacio es para separar los símbolos decodificados simplemente por legibilidad
            aux = ""
    if aux != "":
        raise ValueError("El mensaje no se pudo decodificar completamente.")
    return mensaje_decodificado

if __name__ == "__main__":
    print("a) ", decodificar(MENSAJE_A))
    print("b) ", decodificar(MENSAJE_B))
    print("c) ", decodificar(MENSAJE_C))