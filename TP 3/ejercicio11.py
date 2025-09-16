import importlib.util
import sys
from pathlib import Path

# Ruta absoluta al módulo Utils dentro de la carpeta "TP 2"
module_path = Path("TP 2/Utils.py").resolve()

# Cargar el módulo dinámicamente
spec = importlib.util.spec_from_file_location("Utils", module_path)
Utils = importlib.util.module_from_spec(spec)
sys.modules["Utils"] = Utils
spec.loader.exec_module(Utils)

def entropia_de_la_fuente(probabilidades: list[float], r: int)->float:
    """
    Calcula la entropía de una fuente de información dada su distribución de probabilidades.

    Parámetros:
        - probabilidades (list[float]): Lista de probabilidades de los símbolos de la fuente.
    
    Retorna: un float que representa la entropía de la fuente.
    """
    return Utils.entropia(probabilidades, r)