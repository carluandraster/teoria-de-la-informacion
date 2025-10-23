from ejercicio11 import entropia_a_posteriori
from Utils import entropia
from algebra_lineal.Matriz import Matriz

def resolver(titulo, probabilidades_a_priori, matriz_de_canal):
    print(titulo)
    print(f"Entropía a priori: {entropia(probabilidades_a_priori):.4f}")
    print("Entropías a posteriori:", entropia_a_posteriori(probabilidades_a_priori, matriz_de_canal))
    print("-----------------------")

if __name__ == "__main__":
    resolver("Canal 1", [2/5, 3/5],
             Matriz([[3/5, 2/5],
                     [1/3, 2/3]]))
    resolver("Canal 2", [3/4, 1/4],
             Matriz([[2/3, 1/3],
                     [1/10, 9/10]]))