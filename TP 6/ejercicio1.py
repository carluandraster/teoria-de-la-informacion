from Utils import get_ruido, get_perdida, get_informacion_mutua
from algebra_lineal.Matriz import Matriz
from ejercicio2 import es_canal_sin_ruido, es_canal_determinante

CANAL_1 = Matriz([[0, 1, 0],
                  [0, 0, 1],
                  [0, 1, 0],
                  [1, 0, 0]])

CANAL_2 = Matriz([[1.0, 0.0, 0.0, 0.0],
                  [0.0, 0.2, 0.0, 0.8],
                  [0.0, 0.0, 1.0, 0.0]])

CANAL_3 = Matriz([[0.3, 0.5, 0.2],
                  [0.2, 0.3, 0.5],
                  [0.5, 0.2, 0.3]])

CANAL_4 = Matriz([[0.0, 0.0, 1.0, 0.0],
                  [1.0, 0.0, 0.0, 0.0],
                  [0.0, 1.0, 0.0, 0.0],
                  [0.0, 0.0, 0.0, 1.0]])

def resolver(titulo: str, matriz: Matriz[float]) -> None:
    print(f"--- {titulo} ---")
    probs_a_priori = [1/matriz.cantidadFilas] * matriz.cantidadFilas
    ruido = get_ruido(probs_a_priori, matriz)
    perdida = get_perdida(probs_a_priori, matriz)
    info_mutua = get_informacion_mutua(probs_a_priori, matriz)

    canal_sin_ruido = es_canal_sin_ruido(matriz)
    canal_determinante = es_canal_determinante(matriz)
    if canal_determinante and canal_sin_ruido:
        print("b) El canal es sin ruido y determinante.")
    else:
        if canal_sin_ruido:
            print("b) El canal es sin ruido.")
        else:
            if canal_determinante:
                print("b) El canal es determinante.")
            else:
                print("b) Ninguna.")

    print("Inciso c)")
    print(f"H(A/B) = {ruido:.2f} bits")
    print(f"H(B/A) = {perdida:.2f} bits")
    print(f"I(A,B) = {info_mutua:.2f} bits")
    print("-----------------------------\n")

if __name__ == "__main__":
    resolver("Canal 1", CANAL_1)
    resolver("Canal 2", CANAL_2)
    resolver("Canal 3", CANAL_3)
    resolver("Canal 4", CANAL_4)