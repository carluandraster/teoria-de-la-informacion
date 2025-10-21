from algebra_lineal.Matriz import Matriz
import algebra_lineal.MatrizFactory as mf

def get_matriz_del_canal(entrada: str, salida: str) -> Matriz[float]:
    """
    Genera una matriz de canal a partir de las secuencias de entrada y salida proporcionadas.

    :param entrada: Secuencia de símbolos de entrada.
    :param salida: Secuencia de símbolos de salida.

    :return: Matriz de canal donde cada elemento (i, j) representa la probabilidad
    """
    simbolos_entrada = sorted(set(entrada))
    simbolos_salida = sorted(set(salida))

    filas = len(simbolos_entrada)
    columnas = len(simbolos_salida)

    matriz_canal = mf.ceros(filas, columnas)

    for i, simbolo_entrada in enumerate(simbolos_entrada):
        total_simbolo_entrada = entrada.count(simbolo_entrada)
        for j, simbolo_salida in enumerate(simbolos_salida):
            conteo_conjunto = sum(
                1 for e, s in zip(entrada, salida) if e == simbolo_entrada and s == simbolo_salida
            )
            if total_simbolo_entrada > 0:
                matriz_canal[i][j] = conteo_conjunto / total_simbolo_entrada
            else:
                matriz_canal[i][j] = 0.0

    return matriz_canal