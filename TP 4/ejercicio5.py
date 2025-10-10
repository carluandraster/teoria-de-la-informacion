from Utils import shannon_fano, huffman
from ejercicio1 import primer_teorema_shannon

OMEGA = 0.7
P = [OMEGA, 1-OMEGA]
P_2 = [p1*p2 for p1 in P for p2 in P]

codigo_huffman = huffman(P)
codigo_shannon_fano = shannon_fano(P_2)
print("a) Huffman: ", codigo_huffman)
print("b) Shannon-Fano: ", codigo_shannon_fano)
if primer_teorema_shannon(P, codigo_huffman, 1) and primer_teorema_shannon(P_2, codigo_shannon_fano, 1):
    print("c) Se cumple el primer teorema de Shannon para ambos codigos")
else:
    print("c) No se cumple el primer teorema de Shannon para ambos codigos")