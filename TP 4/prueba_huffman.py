from Utils import huffman

PROBABILIDADES = [0.2, 0.27, 0.4, 0.13]

codigos_huffman = huffman(PROBABILIDADES)
print("Códigos de Huffman:", codigos_huffman)
# Salida esperada: ['111', '10', '0', '110']