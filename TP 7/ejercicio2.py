from CanalFactory import crear_bsc
from Canal import Canal
from segundo_teorema_shannon import get_M

# Datos del ejercicio
p = 0.11
epsilon = 0.1
n = 20
canal = crear_bsc(p)

if __name__ == "__main__":
    C = Canal(canal.get_matriz_canal).capacidad_canal()
    M = get_M(n, C, epsilon)
    print(f"a) Capacidad del canal: {C:.4f} bits por uso")
    print(f"b) R = {C-epsilon:.4f} bits por uso")
    print(f"c) Número máximo de mensajes M para n={n} y ε={epsilon}: {M}")