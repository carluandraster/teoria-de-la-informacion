def huffman(probabilidades: list[float]) -> list[str]:
    """
    Construye un codigo compacto de Huffman a partir de una lista de probabilidades.

    Parámetros:
        - probabilidades (list[float]): Lista de probabilidades de los símbolos de la fuente.
    
    Retorna: lista paralela a 'probabilidades' con las palabras código generadas.
    """

    items = [[p, [i]] for i, p in enumerate(probabilidades)]
    codigos = [''] * len(probabilidades)
    while len(items) > 1:
        items = sorted(items, key=lambda x: x[0])
        menor1 = items.pop(0)
        menor2 = items.pop(0)
        for i in menor1[1]:
            codigos[i] = '0' + codigos[i]
        for i in menor2[1]:
            codigos[i] = '1' + codigos[i]
        items.append([menor1[0] + menor2[0], menor1[1] + menor2[1]])
    return codigos

def _shannon_fano_rec(probabilidades: list[tuple[int, float]], codigos: list[str], prefijo=''):
    N = len(probabilidades)
    if N == 1:
        codigos[probabilidades[0][0]] = prefijo  # Corrección: usar el índice [0] no [1]
    else:
        total = sum(p for _, p in probabilidades)  # Corrección: usar _ para índice y p para probabilidad
        acumulado = 0
        i = 0
        while i < N and acumulado < total / 2:
            acumulado += probabilidades[i][1]
            i += 1
        if i > 0 and i < N:  # Corrección: agregar verificación de límites
            if total/2 - (acumulado - probabilidades[i - 1][1]) < acumulado - total/2:
                i -= 1
        # Corrección: verificar que las divisiones no sean vacías
        if i > 0:
            _shannon_fano_rec(probabilidades[:i], codigos, prefijo + '1')  # Corrección: usar i no i+1
        if i < N:
            _shannon_fano_rec(probabilidades[i:], codigos, prefijo + '0')  # Corrección: usar i no i+1

def shannon_fano(probabilidades: list[float]) -> list[str]:
    """
    Construye un codigo compacto de Shannon-Fano a partir de una lista de probabilidades.

    Parámetros:
        - probabilidades (list[float]): Lista de probabilidades de los símbolos de la fuente.
    
    Retorna: lista paralela a 'probabilidades' con las palabras código generadas.
    """
    indexed_probabilidades = list(enumerate(probabilidades))
    indexed_probabilidades.sort(key=lambda x: x[1], reverse=True)
    codigos = [''] * len(probabilidades)
    _shannon_fano_rec(indexed_probabilidades, codigos)
    return codigos