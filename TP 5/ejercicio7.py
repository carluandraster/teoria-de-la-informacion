from algebra_lineal.Matriz import Matriz

def get_probabilidades_salidas(probabilidades_a_priori: list[float], matriz_canal: Matriz[float]) -> list[float]:
    """
    Calcula las probabilidades de las salidas de un canal de comunicación.

    Parámetros:
    - probabilidades_a_priori: Lista de probabilidades a priori de las entradas.
    - matriz_canal: Matriz de transición del canal, donde cada elemento (i, j)
      representa la probabilidad de que la entrada i produzca la salida j.

    Retorna:
    - Lista de probabilidades de las salidas.
    """
    # Convertir la lista de probabilidades a priori en una matriz columna
    matriz_entradas = Matriz([[p] for p in probabilidades_a_priori])
    
    # Calcular la matriz de probabilidades de salidas
    matriz_salidas = matriz_canal.traspuesta * matriz_entradas

    # Devolver la lista de probabilidades de las salidas
    return [matriz_salidas[i][0] for i in range(matriz_salidas.cantidadFilas)]