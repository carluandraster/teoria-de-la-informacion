from algebra_lineal.Matriz import Matriz
from ejercicio12 import resolver

# Canal 1
PROBS_1 = [0.14, 0.52, 0.34]
MATRIZ_1 = Matriz([[0.5, 0.3, 0.2],
                  [0.0, 0.4, 0.6],
                  [0.2, 0.8, 0.0]])

# Canal 2
PROBS_2 = [0.25, 0.25, 0.50]
MATRIZ_2 = Matriz([[0.25, 0.25, 0.25, 0.25],
                  [0.25, 0.25, 0.00, 0.50],
                  [0.50, 0.00, 0.50, 0.00]])

# Canal 3
PROBS_3 = [0.12, 0.24, 0.14, 0.50]
MATRIZ_3 = Matriz([[0.25, 0.15, 0.30, 0.30],
                  [0.23, 0.27, 0.25, 0.25],
                  [0.10, 0.40, 0.25, 0.25],
                  [0.34, 0.26, 0.20, 0.20]])

if __name__ == "__main__":
    resolver("C1", PROBS_1, MATRIZ_1)
    resolver("C2", PROBS_2, MATRIZ_2)
    resolver("C3", PROBS_3, MATRIZ_3)