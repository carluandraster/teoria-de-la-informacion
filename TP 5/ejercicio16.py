from algebra_lineal.Matriz import Matriz
from Utils import entropia
from ejercicio7 import get_probabilidades_salidas
import ejercicio15 as ej15
from ejercicio13 import PROBS_1, MATRIZ_1, PROBS_2, MATRIZ_2, PROBS_3, MATRIZ_3
from ejercicio14 import PROBS_C1, MAT_C1, PROBS_C2, MAT_C2, PROBS_C3, MAT_C3, PROBS_C4, MAT_C4

def resolver(titulo: str, probs: list[float], matriz: Matriz[float]) -> None:
    print(titulo)
    probabilidades_salidas = get_probabilidades_salidas(probs, matriz)
    print(f"a) H(A) = {entropia(probs):.4f} bits")
    print(f"b) H(B) = {entropia(probabilidades_salidas):.4f} bits")
    print(f"c) H(A/B) = {ej15.get_ruido(probs, matriz):.4f} bits")
    print(f"d) H(B/A) = {ej15.get_perdida(probs, matriz):.4f} bits")
    print(f"e) H(A,B) = {ej15.get_entropia_afin(probs, matriz):.4f} bits")
    print(f"f) I(A,B) = I(B,A) = {ej15.get_informacion_mutua(probs, matriz):.4f} bits")
    print("-----------------\n")

if __name__ == "__main__":
    print("Ejercicio 13: ")
    resolver("Canal 1:", PROBS_1, MATRIZ_1)
    resolver("Canal 2:", PROBS_2, MATRIZ_2)
    resolver("Canal 3:", PROBS_3, MATRIZ_3)
    
    print("Ejercicio 14: ")
    resolver("Canal 1:", PROBS_C1, MAT_C1)
    resolver("Canal 2:", PROBS_C2, MAT_C2)
    resolver("Canal 3:", PROBS_C3, MAT_C3)
    resolver("Canal 4:", PROBS_C4, MAT_C4)