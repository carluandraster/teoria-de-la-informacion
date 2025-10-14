def get_distancia_de_hamming(codigo: list[str]) -> tuple[int, int , int]:
    """Dado un código, devuelve la distancia de Hamming y las cantidades de errores detectables y corregibles.
    
    :param codigo: lista de cadenas que representan las palabras del código
    
    :return: una tupla con la distancia de Hamming, la cantidad de errores detectables y la cantidad de errores corregibles
    """
    distancia_de_haming = float('inf')
    for cod1 in codigo:
        for cod2 in codigo:
            aux = 0
            if cod1 != cod2:
                for i in range(len(cod1)):
                    if cod1[i] != cod2[i]:
                        aux += 1
                if aux < distancia_de_haming:
                    distancia_de_haming = aux