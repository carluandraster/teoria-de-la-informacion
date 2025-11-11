from ejercicio10 import maximizar_informacion_mutua
from algebra_lineal.Matriz import Matriz

CANAL_1 = Matriz([[0.60, 0.40],
                  [0.20, 0.80]])

CANAL_2 = Matriz([[0.25, 0.75],
                  [0.90, 0.10]])

CANAL_3 = Matriz([[0.51, 0.49],
                  [0.72, 0.28]])

CANAL_4 = Matriz([[0.77, 0.23],
                  [0.20, 0.80]])

CANALES = [CANAL_1, CANAL_2, CANAL_3, CANAL_4]

PASO_H = 0.0001

def resolver(titulo, canal):
    print(f"--------{titulo}---------")
    omega_optimo, informacion_mutua_maxima = maximizar_informacion_mutua(canal, PASO_H)
    print(f"w = {omega_optimo:.4f}")
    print(f"C = {informacion_mutua_maxima:.4f} bits\n")

if __name__ == "__main__":
    for i, canal in enumerate(CANALES, start=1):
        resolver(f"Canal {i}", canal) 