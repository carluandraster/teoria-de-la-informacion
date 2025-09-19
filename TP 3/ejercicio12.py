import ejercicio9 as ej9
import ejercicio11 as ej11

# Constantes
PROBABILIDADES = [0.10, 0.50, 0.10, 0.20, 0.05, 0.05]
CODIGO1  = ["==", "<", "<=", ">", ">=", "<>"]
CODIGO2  = [")", "[]", "]]", "([", "[()]", "([)]"]
CODIGO3  = ["/", "*", "-", "*", "++", "+-"]
CODIGO4  = [".,", ";", ",,", ":", "...", ",:;"]

# Funciones
def get_respuesta(codigo, probabilidades):
    return f'''H(S) = {ej11.entropia_de_la_fuente(codigo, probabilidades)}\nL = {ej11.get_longitud_media(codigo, probabilidades)}'''

print("Codigo 1\n", get_respuesta(CODIGO1, PROBABILIDADES), "\n", sep="")
print("Codigo 2\n", get_respuesta(CODIGO2, PROBABILIDADES), "\n", sep="")
print("Codigo 3\n", get_respuesta(CODIGO3, PROBABILIDADES), "\n", sep="")
print("Codigo 4\n", get_respuesta(CODIGO4, PROBABILIDADES), "\n", sep="")