import ejercicio14 as ej14
from Matriz import Matriz

print("Grafo 2")
matriz_de_transiciones = Matriz(4,4,[[0.5, 0, 0, 0.5],
                                      [0.5, 0, 0, 0],
                                      [0, 0.5, 0, 0],
                                      [0, 0.5, 1, 0.5]])
print("Vector estacionario:")
print(ej14.estadosEstables(matriz_de_transiciones))
print("Entropía de la fuente: ", ej14.entropiaMarkoviana(matriz_de_transiciones), " bits")