from Utils import getAlfaProbabilidades
from ejercicio11 import huffman, shannon_fano

def engine(texto: str) -> None:
    alfabeto, probabilidades = getAlfaProbabilidades(texto)
    
    # Obtener índices de ordenamiento
    indices_ordenados = sorted(range(len(alfabeto)), key=lambda i: alfabeto[i])
    # Ordenar probabilidades según los índices obtenidos
    alfabeto_ordenado = [alfabeto[i] for i in indices_ordenados]
    probabilidades_ordenadas = [probabilidades[i] for i in indices_ordenados]
    
    print("Símbolos\t\t  ", "\t".join(alfabeto_ordenado))
    print(f"Fuente con Huffman: \t ", "\t".join(huffman(probabilidades_ordenadas)))
    print(f"Fuente con Shannon-Fano: ", "\t".join(shannon_fano(probabilidades_ordenadas)))

if __name__ == "__main__":
    print("Inciso a")
    engine("ABCDABCBDCBAAABBBCBCBABADBCBABCBDBCCCAAABB")
    print("Inciso b")
    engine("AOEAOEOOOOEOAOEOOEOOEOAOAOEOEUUUIEOEOEO")