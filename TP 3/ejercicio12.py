import ejercicio11 as ej11

PROBABILIDADES = [0.10, 0.50, 0.10, 0.20, 0.05, 0.05]
CODIGO1  = ["==", "<", "<=", ">", ">=", "<>"]
CODIGO2  = [")", "[]", "]]", "([", "[()]", "([)]"]
CODIGO3  = ["/", "*", "-", "*", "++", "+-"]
CODIGO4  = [".,", ";", ",,", ":", "...", ",:;"]

print("Entropía de la fuente:", ej11.entropia_de_la_fuente(PROBABILIDADES))
print("Longitud media del código 1:", ej11.get_longitud_media(CODIGO1, PROBABILIDADES))
print("Longitud media del código 2:", ej11.get_longitud_media(CODIGO2, PROBABILIDADES))
print("Longitud media del código 3:", ej11.get_longitud_media(CODIGO3, PROBABILIDADES))
print("Longitud media del código 4:", ej11.get_longitud_media(CODIGO4, PROBABILIDADES))