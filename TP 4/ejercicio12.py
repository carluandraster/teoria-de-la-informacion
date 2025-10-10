import ejercicio11 as ej11
from Utils import entropia, get_longitud_media
from ejercicio6 import get_rendimiento_y_redundancia

P = [0.385, 0.154, 0.128, 0.154, 0.179]

print(f"a) Entropia de la fuente: {entropia(P):.4f}")
codigo_huffman = ej11.huffman(P)
print(f"b) Codificación de Huffman: {codigo_huffman}")
codigo_shannon_fano = ej11.shannon_fano(P)
print(f"c) Codificación de Shannon-Fano: {codigo_shannon_fano}")
print("e)\tLongitud media\tRendimiento\tRedundancia")
print(f"Huffman\t{get_longitud_media(codigo_huffman, P):.4f}\t{"\t".join(map(str, get_rendimiento_y_redundancia(P, codigo_huffman)))}")
print(f"Shannon-Fano\t{get_longitud_media(codigo_shannon_fano, P):.4f}\t{"\t".join(map(str, get_rendimiento_y_redundancia(P, codigo_shannon_fano)))}")