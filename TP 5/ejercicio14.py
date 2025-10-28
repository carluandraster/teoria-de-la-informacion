from algebra_lineal.Matriz import Matriz
from Utils import entropia
from ejercicio7 import get_probabilidades_salidas

# Probabilidades a priori
PROBS_C1 = [0.70, 0.30]
PROBS_C2 = [0.50, 0.50]
PROBS_C3 = [0.25, 0.50, 0.25]
PROBS_C4 = [0.25, 0.25, 0.25, 0.25]

# Matrices asociadas a los canales de comunicación
MAT_C1 = Matriz([
    [0.7, 0.3],
    [0.4, 0.6]
])

MAT_C2 = Matriz([
    [0.3, 0.3, 0.4],
    [0.3, 0.3, 0.4]
])

MAT_C3 = Matriz([
    [1.0, 0.0, 0.0, 0.0],
    [0.0, 0.5, 0.5, 0.0],
    [0.0, 0.0, 0.0, 1.0]
])

MAT_C4 = Matriz([
    [1.0, 0.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 0.0, 1.0]
])

def resolver(titulo: str, probs: list[float], matriz: Matriz[float]) -> None:
    print(titulo)
    print(f"H(A) = {entropia(probs):.4f} bits")
    print(f"H(B) = {entropia(get_probabilidades_salidas(probs, matriz)):.4f} bits")
    print("-----------------\n")

resolver("C1", PROBS_C1, MAT_C1)
resolver("C2", PROBS_C2, MAT_C2)
resolver("C3", PROBS_C3, MAT_C3)
resolver("C4", PROBS_C4, MAT_C4)