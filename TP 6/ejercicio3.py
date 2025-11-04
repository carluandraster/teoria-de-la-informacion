from Utils import get_ruido, get_informacion_mutua, get_probabilidades_salidas
from algebra_lineal.Matriz import Matriz

A = [0.5, 0.5]  # Distribución de probabilidad de la fuente
PRIMER_CANAL = Matriz([[0.7, 0.0, 0.3, 0.0],
                        [0.2, 0.6, 0.0, 0.2]])
B = get_probabilidades_salidas(A, PRIMER_CANAL)
SEGUNDO_CANAL = Matriz([[0.9, 0.0, 0.1],
                        [0.0, 1.0, 0.0],
                        [0.1, 0.1, 0.8],
                        [0.0, 0.5, 0.5]])

def escribir_equivocacion_e_info_mutua(titulo: str, probs_a_priori: list[float], matriz_del_canal: Matriz[float]) -> None:
    ruido = get_ruido(probs_a_priori, matriz_del_canal)
    info_mutua = get_informacion_mutua(probs_a_priori, matriz_del_canal)
    print(f"{titulo}")
    print(f"H(A/B) = {ruido:.4f} bits")
    print(f"I(A,B) = {info_mutua:.4f} bits\n")
    print("-" * 30 + "\n")

if __name__ == "__main__":
    print("Inciso a)")
    escribir_equivocacion_e_info_mutua("Primer Canal:", A, PRIMER_CANAL)
    escribir_equivocacion_e_info_mutua("Segundo Canal:", B, SEGUNDO_CANAL)
    matriz_compuesta = PRIMER_CANAL * SEGUNDO_CANAL

    print("b) Matriz compuesta del canal:")
    print(matriz_compuesta, "\n")

    print("Inciso c)")
    escribir_equivocacion_e_info_mutua("Canal Compuesto:", A, matriz_compuesta)