from typing import Tuple
from Utils import entropia_de_la_fuente, get_longitud_media

def get_rendimiento_y_redundancia(probabilidades: list, codificacion: list) -> Tuple[float, float]:
    """
    Calcula el rendimiento y la redundancia de una codificación.
    
    Parámetros:
        - probabilidades (list): Lista de probabilidades de los símbolos.
        - codificacion (list): Lista de longitudes de los códigos para cada símbolo.
    
    Retorna: rendimiento (float), redundancia (float)
    """
    H = entropia_de_la_fuente(codificacion, probabilidades)
    L = get_longitud_media(codificacion, probabilidades)
    RENDIMIENTO = H / L
    return RENDIMIENTO, 1-RENDIMIENTO