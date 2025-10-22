from ejercicio1 import ENTRADA, SALIDA
from ejercicio3 import CANAL1, CANAL2
from Canal import Canal
from Utils import get_frecuencias_relativas
from ejercicio7 import get_probabilidades_salidas

def resolver(titulo: str, entrada: str, salida: str) -> None:
    CANAL = Canal(entrada, salida)
    print(titulo)
    print("Probabilidades de los símbolos de salida:")
    print("Sacando frecuencias relativas: ", dict(sorted(get_frecuencias_relativas(salida).items())))
    probabilidades_a_priori = dict(sorted(get_frecuencias_relativas(entrada).items())).values()
    matriz = CANAL.get_matriz_del_canal()
    print("Teniendo en cuenta las probabilidades a priori y la matriz del canal: ",
          get_probabilidades_salidas(probabilidades_a_priori, matriz))

if __name__ == "__main__":
    resolver("Ejercicio 1", ENTRADA, SALIDA)
    resolver("Ejercicio 3 - Canal 1", CANAL1.get_entrada, CANAL1.get_salida)
    resolver("Ejercicio 3 - Canal 2", CANAL2.get_entrada, CANAL2.get_salida)