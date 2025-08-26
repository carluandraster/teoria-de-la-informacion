import math

# Función para calcular la cantidad de información
# p: probabilidad del evento
# r: base del logaritmo (default 2)
# retorna la cantidad de información en bits (si r=2)
def cantidadInformacion(p: float, r=2) -> float:
    if p <= 0 or p > 1:
        resultado = 0
    else:
        resultado = math.log(1/p, r)
    return resultado

# Funcion para calcular entropia
# probabilidades: lista de probabilidades de los eventos
# r: base del logaritmo (default 2)
# retorna la entropia en bits (si r=2)
def entropia(probabilidades: list, r=2) -> float:
    H = 0
    for p in probabilidades:
        H += p * cantidadInformacion(p, r)
    return H