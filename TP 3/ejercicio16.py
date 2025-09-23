import random

def simular_fuente(codigos: list[str], probabilidades: list[float], n: int) -> list[str]:
    """
    Simula la salida de una fuente de información discreta.

    Parameteros:
        - codigos: lista de símbolos del código.
        - probabilidades: lista de probabilidades asociadas a cada símbolo.
        - n: cantidad de símbolos a simular.
    
    Retorna: (list[str]) lista de símbolos simulados.

    Contrato:
        - len(codigos) > 0
        - len(probabilidades) > 0
        - len(codigos) == len(probabilidades)
        - sum(probabilidades) == 1
        - all(p >= 0 and p <= 1 for p in probabilidades)
        - n > 0
    """
    simulacion = []
    for _ in range(n):
        simulacion.append(random.choices(codigos, weights=probabilidades)[0])
    return simulacion