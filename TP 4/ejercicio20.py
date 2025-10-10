from ejercicio19 import comprimir_con_rlc
from ejercicio16 import get_tasa_de_compresion

MENSAJE_A = "XXXYZZZZ"
MENSAJE_B = "AAAABBBCCDAA"
MENSAJE_C = "UUOOOOAAAIEUUUU"

def engine(inciso: str, mensaje: str) -> None:
    print(f"Inciso {inciso}")
    print(f"Mensaje original: {mensaje}")
    mensaje_comprimido = comprimir_con_rlc(mensaje)
    mensaje_rlc = ""
    for i, val in enumerate(mensaje_comprimido):
        if i % 2 == 0:
            mensaje_rlc += chr(int(val))
        else:
            mensaje_rlc += str(int(val))
    print(f"Mensaje comprimido (RLC): {mensaje_rlc}")
    tasa_de_compresion = get_tasa_de_compresion(mensaje, mensaje_comprimido)
    print(f"Tasa de compresion: {tasa_de_compresion:.2f}")
    print("-" * 40)

engine("a)", MENSAJE_A)
engine("b)", MENSAJE_B)
engine("c)", MENSAJE_C)