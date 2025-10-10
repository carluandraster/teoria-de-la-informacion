from Utils import entropia_de_la_fuente, get_longitud_media, get_alfaprobabilidades_ordenado
from ejercicio6 import get_rendimiento_y_redundancia
from ejercicio11 import huffman, shannon_fano

MENSAJE = "58784784525368669895745123656253698989656452121702300223659"

if __name__ == "__main__":
    H = entropia_de_la_fuente(MENSAJE)
    print(f"a) Entropía de la fuente: {H:.4f} bits/símbolo")

    # Obtener alfabeto y probabilidades
    alfabeto, probabilidades = get_alfaprobabilidades_ordenado(MENSAJE)
    print(f"   Alfabeto: {alfabeto}")
    
    # Codificaciones
    codigo_huffman = huffman(probabilidades)
    print(f"b) Código de Huffman: {codigo_huffman}")
    
    codigo_shannon_fano = shannon_fano(alfabeto, probabilidades)
    print(f"c) Código de Shannon-Fano: {codigo_shannon_fano}")
    
    print("e)\tLongitud media\tRendimiento\tRedundancia")
    
    longitud_media = get_longitud_media(codigo_huffman, probabilidades)
    rendimiento, redundancia = get_rendimiento_y_redundancia(probabilidades, codigo_huffman)
    print(f"Huffman\t{longitud_media:.4f}\t{rendimiento:.4f}\t{redundancia:.4f}")
    
    longitud_media = get_longitud_media(codigo_shannon_fano, probabilidades)
    rendimiento, redundancia = get_rendimiento_y_redundancia(probabilidades, codigo_shannon_fano)
    print(f"Shannon-Fano\t{longitud_media:.4f}\t{rendimiento:.4f}\t{redundancia:.4f}")