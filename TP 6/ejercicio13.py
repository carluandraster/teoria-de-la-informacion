from ejercicio14 import prob_error_canal
from algebra_lineal.Matriz import Matriz

CANAL = Matriz([[0.6, 0.3, 0.1],
                [0.1, 0.8, 0.1],
                [0.3, 0.3, 0.4]])

PROBS_A_PRIORI_A = [1/3, 1/3, 1/3]
PROBS_A_PRIORI_B = [1/8, 3/8, 4/8]
PROBS_A_PRIORI_C = [4/15, 3/15, 8/15]

if __name__ == "__main__":
    aprioris = [PROBS_A_PRIORI_A, PROBS_A_PRIORI_B, PROBS_A_PRIORI_C]
    for apriori in aprioris:
        print(f"P_E = {prob_error_canal(apriori, CANAL):.4f}")