import ejercicio14 as ej14

# Constantes
PROBABILIDADES = [0.10, 0.50, 0.10, 0.20, 0.05, 0.05]
CODIGO1  = ["==", "<", "<=", ">", ">=", "<>"]
CODIGO2  = [")", "[]", "]]", "([", "[()]", "([)]"]
CODIGO3  = ["/", "*", "-", "*", "++", "+-"]
CODIGO4  = [".,", ";", ",,", ":", "...", ",:;"]

# Funciones
def get_respuesta(codigos: list[str], probabilidades: list[float]) -> str:
    """Devuelve una respuesta acorde a lo que pide el ejercicio.
    """
    if ej14.es_codigo_compacto(codigos, probabilidades):
        return "Compacto"
    else:
        return "No"
    
print(get_respuesta(CODIGO1, PROBABILIDADES))
print(get_respuesta(CODIGO2, PROBABILIDADES))
print(get_respuesta(CODIGO3, PROBABILIDADES))
print(get_respuesta(CODIGO4, PROBABILIDADES))