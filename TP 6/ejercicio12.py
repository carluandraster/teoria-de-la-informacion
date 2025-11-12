from ejercicio14 import prob_error_canal
from algebra_lineal.Matriz import Matriz

CANAL = Matriz([[0.6, 0.4],
                [0.2, 0.8]])
PROBS_A_PRIORI = [0.5, 0.5]

if __name__ == "__main__":
    print(f"P_E = {prob_error_canal(PROBS_A_PRIORI, CANAL):.4f}")