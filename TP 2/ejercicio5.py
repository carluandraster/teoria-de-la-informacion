import Utils

cadena = "ABDAACAABACADAABDAADABDAAABDCDCDCDC"
alfabeto, probabilidades = Utils.getAlfaProbabilidades(cadena)
print("Probabilidades:", dict(zip(alfabeto, probabilidades)))
print("Entropía:", Utils.entropia(probabilidades))