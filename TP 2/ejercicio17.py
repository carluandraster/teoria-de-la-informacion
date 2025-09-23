import ejercicio14 as ej14
from Matriz import Matriz

print("Grafo 2")
matriz_de_transiciones = Matriz([[0.5, 0, 0, 0.5],
                                [0.5, 0, 0, 0],
                                [0, 0.5, 0, 0],
                                [0, 0.5, 1, 0.5]])
print("Vector estacionario:")
print(ej14.estadosEstables(matriz_de_transiciones))
print("Entropía de la fuente: ", ej14.entropiaMarkoviana(matriz_de_transiciones), " bits\n")

print("Grafo 3")
matriz_de_transiciones = Matriz([[1/3, 0, 1, 1/2, 0],
                                [1/3, 0, 0, 0, 0],
                                [0, 1, 0, 0, 0],
                                [1/3, 0, 0, 0, 1/2],
                                [0, 0, 0, 1/2, 1/2]])
print("Vector estacionario:")
print(ej14.estadosEstables(matriz_de_transiciones))
print("Entropía de la fuente: ", ej14.entropiaMarkoviana(matriz_de_transiciones), " bits\n")