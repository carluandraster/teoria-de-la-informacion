from ejercicio6 import get_rendimiento_y_redundancia

PROBABILIDADES = [0.2, 0.15, 0.1, 0.3, 0.25]
CODIGO1  = ["01", "111", "110", "101", "100"]
CODIGO2  = ["00", "01", "10", "110", "111"]
CODIGO3  = ["0110", "010", "0111", "1", "00"]
CODIGO4  = ["11", "001", "000", "10", "01"]

if __name__ == "__main__":
    print("Código\t\tRendimiento\tRedundancia")
    rendimiento1, redundancia1 = get_rendimiento_y_redundancia(PROBABILIDADES, CODIGO1)
    print(f"Código 1\t{rendimiento1:.4f}\t\t{redundancia1:.4f}")

    rendimiento2, redundancia2 = get_rendimiento_y_redundancia(PROBABILIDADES, CODIGO2)
    print(f"Código 2\t{rendimiento2:.4f}\t\t{redundancia2:.4f}")

    rendimiento3, redundancia3 = get_rendimiento_y_redundancia(PROBABILIDADES, CODIGO3)
    print(f"Código 3\t{rendimiento3:.4f}\t\t{redundancia3:.4f}")

    rendimiento4, redundancia4 = get_rendimiento_y_redundancia(PROBABILIDADES, CODIGO4)
    print(f"Código 4\t{rendimiento4:.4f}\t\t{redundancia4:.4f}")