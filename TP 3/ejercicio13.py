import math

# Constantes
PROBABILIDADES_FUENTE1 = [0.5, 0.25, 0.125, 0.125]
PROBABILIDADES_FUENTE2 = [0.333, 0.333, 0.167, 0.167]

# Funciones
def get_longitudes_maximas(probabilidades: list[float], r: int) -> list[int]:
    """Calculas las longitudes máximas que debe tener un código para ser compacto
    
    Parametros:
        - probabilidades: lista de probabilidades de los símbolos
        - r: base del código (2 para binario, 3 para ternario, etc.)
    
    Retorna: lista de longitudes máximas para cada símbolo
    
    Contrato:
        - probabilidades es distinta de None y no es una lista vacía
        - todos los elementos de probabilidades son mayores que 0 y menores o iguales que 1
        - la suma de los elementos de probabilidades es igual a 1
        - Se devuelve una lista de enteros positivos
        - r es un entero mayor que 1
    """
    longitudes = []
    for p in probabilidades:
        l = math.ceil(-math.log(p, r))
        longitudes.append(l)
    return longitudes

# Main
longitudes_maximas1 = get_longitudes_maximas(PROBABILIDADES_FUENTE1, 2)
longitudes_maximas2 = get_longitudes_maximas(PROBABILIDADES_FUENTE2, 2)
print("a) Utilizando el alfabeto código binario:")
print(f"   Longitudes máximas fuente 1: {longitudes_maximas1}")
print(f"   Longitudes máximas fuente 2: {longitudes_maximas2}")

longitudes_maximas1 = get_longitudes_maximas(PROBABILIDADES_FUENTE1, 3)
longitudes_maximas2 = get_longitudes_maximas(PROBABILIDADES_FUENTE2, 3)
print("b) Utilizando el alfabeto código ternario:")
print(f"   Longitudes máximas fuente 1: {longitudes_maximas1}")
print(f"   Longitudes máximas fuente 2: {longitudes_maximas2}")