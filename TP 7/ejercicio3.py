from ejercicio2 import epsilon
from segundo_teorema_shannon import get_M

# Datos del ejercicio
C = 0.5
n = 10

if __name__ == "__main__":
    m = get_M(n, C, epsilon)
    print(f"Número máximo de mensajes M para n={n} y ε={epsilon}: {m}")
    n = 1000
    m = get_M(n, C, epsilon)
    print(f"Número máximo de mensajes M para n={n} y ε={epsilon}: {m}")