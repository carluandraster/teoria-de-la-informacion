import Utils

print("La máxima entropía es 2 bits por ser el logaritmo base 2 de 4 estados posibles.")
entropia = Utils.entropia([0.25, 0.25, 0.25, 0.25])
print(entropia)
print("Para ello, los 4 estados deben ser equiprobables.")