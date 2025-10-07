import Utils
from ejercicio1 import primer_teorema_shannon

OMEGA = 0.8
PROBS = [OMEGA, 1-OMEGA]
CODIGO = ["0", "1"]

codificacion, probabilidades = Utils.generarConExtension(["0", "1"], PROBS, 3)
print("Codificacion: ", codificacion)
if(primer_teorema_shannon(PROBS, CODIGO, 3)):
    print("La codificacion propuesta ya cumple el primer teorema de Shannon")
else:
    print("La codificacion propuesta no cumple el primer teorema de Shannon")