from segundo_teorema_shannon import get_M
from typing import Callable
from pandas import DataFrame

get_R: Callable[[float, float], float] = lambda C, epsilon: C - epsilon
def progress_bar(percentage: float, length: int = 20) -> str:
    filled = int(length * percentage / 100)
    bar = '█' * filled + ' ' * (length - filled)
    return f"[{bar}]"

if __name__ == "__main__":
    C = float(input("C = "))
    n = int(input("n = "))
    rows: list[dict[str, float | str]] = []
    epsilon = 0.01
    h = 0.01
    while epsilon < 0.5:
        M = get_M(n, C, epsilon)
        R = get_R(C, epsilon)
        uso_capacidad_total = (R / C) * 100
        # Función para crear una barra de progreso
        
        rows.append(
            {
                "ε": round(epsilon, 4),
                "M": f"{M:.2e}",
                "R": round(R, 4),
                "Uso de la capacidad total": progress_bar(uso_capacidad_total),
            }
        )
        epsilon += h
    df = DataFrame(rows, columns=["ε", "M", "R", "Uso de la capacidad total"])
    print(df)