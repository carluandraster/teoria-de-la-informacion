import ejercicio7 as ej7
from algebra_lineal.Matriz import Matriz

PROBABILIDADES_A_PRIORI = [0.3, 0.3, 0.4]
MATRIZ_CANAL = Matriz([[0.4, 0.4, 0.2],
                      [0.3, 0.2, 0.5],
                      [0.3, 0.4, 0.3]])

if __name__ == "__main__":
      print("a) Probabilidades de los simbolos de salida: ",
            ej7.get_probabilidades_salidas(PROBABILIDADES_A_PRIORI, MATRIZ_CANAL))

      print("b) Probabilidades a posteriori: \n",
            ej7.get_probabilidades_a_posteriori(PROBABILIDADES_A_PRIORI, MATRIZ_CANAL))

      print("c) Probabilidades de eventos simultaneos: \n",
            ej7.get_probabilidades_eventos_simultaneos(PROBABILIDADES_A_PRIORI, MATRIZ_CANAL))