import ejercicio11 as ej11
from ejercicio15 import Decodificador
from ejercicio6 import get_rendimiento_y_redundancia
from ejercicio16 import get_tasa_de_compresion

SIMBOLOS = [
    " ", ",", ".", ":", ";",
    "A", "B", "C", "D", "E",
    "F", "G", "H", "I", "J",
    "K", "L", "M", "N", "Ñ",
    "O", "P", "Q", "R", "S",
    "T", "U", "V", "W", "X",
    "Y", "Z"
]
PROBABILIDADES = [
    0.175990, 0.014093, 0.015034, 0.000542, 0.002109,
    0.111066, 0.015368, 0.030176, 0.038747, 0.101604,
    0.004873, 0.008762, 0.007953, 0.049740, 0.003706,
    0.000034, 0.048149, 0.021041, 0.050490, 0.002018,
    0.073793, 0.019583, 0.010246, 0.051446, 0.058406,
    0.031093, 0.033240, 0.008930, 0.000012, 0.000706,
    0.007851, 0.003199
]

def generar_codificacion(probabilidades: list) -> tuple[list[str], float]:
    """
    Genera una codificación binaria óptima utilizando el algoritmo de Huffman o Shannon-Fano,
    dependiendo del rendimiento.
    
    :param probabilidades: Lista de probabilidades de los símbolos.
    :return: Una tupla que contiene la lista de códigos generados y el rendimiento.
    """
    codificacion_huffman = ej11.huffman(probabilidades)
    rendimiento_huffman, _ = get_rendimiento_y_redundancia(probabilidades, codificacion_huffman)

    codificacion_shannon_fano = ej11.shannon_fano(probabilidades)
    rendimiento_shannon_fano, _ = get_rendimiento_y_redundancia(probabilidades, codificacion_shannon_fano)

    if rendimiento_huffman >= rendimiento_shannon_fano:
        return codificacion_huffman, rendimiento_huffman
    else:
        return codificacion_shannon_fano, rendimiento_shannon_fano

if __name__ == "__main__":
    codificacion, rendimiento = generar_codificacion(PROBABILIDADES)
    print("Rendimiento: {:.4f}".format(rendimiento))
    decodificador = Decodificador(SIMBOLOS, codificacion)
    mensaje = input("Ingrese un mensaje: ")
    mensaje_codificado = decodificador.codificar(mensaje)
    
    # Persistir en archivo binario
    nombre_archivo = "mensaje_codificado.dat"
    with open(nombre_archivo, 'wb') as archivo:
        archivo.write(mensaje_codificado)