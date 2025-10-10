from ejercicio17 import generar_codificacion, SIMBOLOS, PROBABILIDADES
from ejercicio15 import Decodificador

if __name__ == "__main__":
    codificacion, _ = generar_codificacion(PROBABILIDADES)
    decodificador = Decodificador(SIMBOLOS, codificacion)

    # Cargar mensaje codificado desde archivo
    nombre_archivo = "TP 4/mensaje_codificado.dat"
    with open(nombre_archivo, 'rb') as archivo:
        mensaje_codificado = archivo.read()

    mensaje_decodificado = decodificador.decodificar(mensaje_codificado)
    print("Mensaje decodificado:", mensaje_decodificado)