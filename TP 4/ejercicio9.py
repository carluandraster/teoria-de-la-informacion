from ejercicio11 import shannon_fano, huffman

FUENTE_A = [0.2, 0.2, 0.3, 0.3]
FUENTE_B = [0.4, 0.25, 0.25, 0.1]

def engine(nombre: str, probabilidades: list[float])->None:
    print(f"Fuente {nombre} con Huffman: ", huffman(probabilidades))
    print(f"Fuente {nombre} con Shannon-Fano: ", shannon_fano(probabilidades))

if __name__ == "__main__":
    engine("A", FUENTE_A)
    engine("B", FUENTE_B)