from Utils import get_probabilidades_a_posteriori
from algebra_lineal.Matriz import Matriz

CANAL = Matriz([[0.6, 0.4],
                [0.2, 0.8]])
PROBS_A_PRIORI = [0.5, 0.5]

if __name__ == "__main__":
    print(get_probabilidades_a_posteriori(PROBS_A_PRIORI, CANAL).redondear(4))