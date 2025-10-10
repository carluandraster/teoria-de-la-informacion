from ejercicio3 import C1, C2, P, P_2
from ejercicio6 import get_rendimiento_y_redundancia

def engine(nombre:str, probabilidades:list, codificacion1:list):
    rendimiento, redundancia = get_rendimiento_y_redundancia(probabilidades, codificacion1)
    print(f"Código {nombre}")
    print(f"Rendimiento: {rendimiento:.4f}")
    print(f"Redundancia: {redundancia:.4f}\n")

engine("C1", P, C1)
engine("C2", P_2, C2)