import Utils

# Devuelve un string con la cantidad de informacion de cada simbolo del alfabeto y su entropía
def obtenerDatos(alfabeto: list, probabilidades: list):
    informacion = "Simbolo\tProbabilidad\tInformación\n"
    entropia = Utils.entropia(probabilidades)
    for i in range(len(alfabeto)):
        info = Utils.cantidadInformacion(probabilidades[i])
        informacion += f"{alfabeto[i]}\t{probabilidades[i]:.4f}\t\t{info:.4f}\n"
    informacion += f"Entropía: {entropia:.4f} bits"
    return informacion

print(obtenerDatos(['x','y','z'], [0.5, 0.1, 0.4]),"\n")
print(obtenerDatos([0,1], [0.5, 0.5]),"\n")
print(obtenerDatos(['A','B','C','D'], [0.1, 0.3, 0.4, 0.2]),"\n")