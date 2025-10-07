def generar_combinaciones(alfabeto: list, N: int) -> list:
    """Genera todas las combinaciones posibles de longitud N
    a partir del alfabeto dado.
    
    Parametros:
        alfabeto (list): lista de elementos del alfabeto
        N (int): longitud de las combinaciones a generar
    Retorna:
        list: lista de combinaciones generadas
    """
    if N == 1:
        return [[letra] for letra in alfabeto]
    else:
        combinaciones_previas = generar_combinaciones(alfabeto, N - 1)
        nuevas_combinaciones = []
        for combinacion in combinaciones_previas:
            for letra in alfabeto:
                nuevas_combinaciones.append(combinacion + [letra])
        return nuevas_combinaciones

def generarConExtension(alfabeto: list, probabilidades: list[float], N: int):
    """Genera el alfabeto y la distribución de probabilidades
    de una fuente con extensión de orden N.
    
    Parámetros:
        alfabeto (list): lista de elementos del alfabeto
        probabilidades (list[float]): lista de probabilidades de cada elemento del alfabeto
        N (int): orden de la extensión
    Retorna:
        tuple: (nuevas_letras, nuevas_probabilidades)
    """
    if N <= 0:
        return [], []

    # Generar las combinaciones de longitud N
    combinaciones = generar_combinaciones(alfabeto, N)

    # Calcular las probabilidades de cada combinación
    nuevas_probabilidades = []
    for combinacion in combinaciones:
        probabilidad = 1.0
        for letra in combinacion:
            indice = alfabeto.index(letra)
            probabilidad *= probabilidades[indice]
        nuevas_probabilidades.append(probabilidad)

    # Convertir las combinaciones de listas de letras a cadenas
    nuevas_letras = [''.join(str(combinacion)) for combinacion in combinaciones]

    return nuevas_letras, nuevas_probabilidades