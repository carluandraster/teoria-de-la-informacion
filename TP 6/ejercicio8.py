from ejercicio1 import CANAL_1, CANAL_2, CANAL_3, CANAL_4
from ejercicio9 import capacidad_canal

CANALES = [CANAL_1, CANAL_2, CANAL_3, CANAL_4]

if __name__ == "__main__":
    for i, canal in enumerate(CANALES, start=1):
        capacidad = capacidad_canal(canal)
        print(f"Capacidad del CANAL_{i}: {capacidad:.4f} bits")