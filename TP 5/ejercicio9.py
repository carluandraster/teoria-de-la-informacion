from ejercicio1 import ENTRADA, SALIDA
from ejercicio2 import get_matriz_del_canal
from ejercicio3 import CANAL1, CANAL2
from ejercicio7 import get_probabilidades_a_posteriori, get_probabilidades_eventos_simultaneos
from Utils import get_frecuencias_relativas

def resolver(titulo: str, entrada: str, salida: str) -> None:
    matriz = get_matriz_del_canal(entrada, salida)
    probabilidades_entrada = list(dict(sorted(get_frecuencias_relativas(entrada).items())).values())
    print(f"\n--- {titulo} ---")
    print("Probabilidades a posteriori:")
    print(get_probabilidades_a_posteriori(probabilidades_entrada, matriz))
    print("Probabilidades de eventos simultáneos:")
    print(get_probabilidades_eventos_simultaneos(probabilidades_entrada, matriz))

if __name__ == "__main__":
    resolver("Ejercicio 1", ENTRADA, SALIDA)
    resolver("Ejercicio 3 - Canal 1", CANAL1.get_entrada, CANAL1.get_salida)
    resolver("Ejercicio 3 - Canal 2", CANAL2.get_entrada, CANAL2.get_salida)