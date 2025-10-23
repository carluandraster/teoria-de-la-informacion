from ejercicio1 import ENTRADA, SALIDA
from ejercicio2 import get_matriz_del_canal
from ejercicio3 import CANAL1, CANAL2
from ejercicio6 import PROBABILIDADES_A_PRIORI, MATRIZ_CANAL
from ejercicio11 import entropia_a_posteriori
from Utils import entropia, get_frecuencias_relativas

def resolver(titulo, a_priori, matriz):
    print(titulo)
    print("Entropía a priori: ", entropia(a_priori))
    print("Entropía a posteriori: ", entropia_a_posteriori(a_priori, matriz))
    print("-----------------\n")

if __name__ == "__main__":
    resolver("Ejercicio 1", get_frecuencias_relativas(ENTRADA), get_matriz_del_canal(ENTRADA, SALIDA))
    resolver("Ejercicio 3 - Canal 1", get_frecuencias_relativas(CANAL1.get_entrada), get_matriz_del_canal(CANAL1.get_entrada, CANAL1.get_salida))
    resolver("Ejercicio 3 - Canal 2", get_frecuencias_relativas(CANAL2.get_entrada), get_matriz_del_canal(CANAL2.get_entrada, CANAL2.get_salida))
    resolver("Ejercicio 6", PROBABILIDADES_A_PRIORI, MATRIZ_CANAL)