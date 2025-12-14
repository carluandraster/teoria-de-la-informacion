from segundo_teorema_shannon import get_M
from math import log, floor

# Datos del problema
C = 1
n = 100
epsilon = 0.5

M_A = get_M(n, C, epsilon)
print(f"a) M = {M_A:.2e}")
epsilon = 0.01
M_B = get_M(n, C, epsilon)
print(f"b) M = {M_B:.2e}")
print("Ordenes de magnitud de diferencia: ", floor(log(M_B // M_A, 10)))