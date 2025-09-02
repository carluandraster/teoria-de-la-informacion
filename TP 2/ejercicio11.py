import ejercicio10 as ej10
import Utils

alfabeto = [i for i in range(1,7)]

print("Inciso a")
probabilidades = [1/6 for _ in range(6)]
print("H(S) =", Utils.entropia(probabilidades))
extension, probabilidadesCombinadas = ej10.generarConExtension(alfabeto, probabilidades, 2)
print("H(S_2) =", Utils.entropia(probabilidadesCombinadas))
extension, probabilidadesCombinadas = ej10.generarConExtension(alfabeto, probabilidades, 3)
print("H(S_3) =", Utils.entropia(probabilidadesCombinadas),"\n")

print("Inciso b")
probabilidades = [1/9, 1/6, 1/9, 1/9, 1/6, 1/3]
print("H(S) =", Utils.entropia(probabilidades))
extension, probabilidadesCombinadas = ej10.generarConExtension(alfabeto, probabilidades, 2)
print("H(S_2) =", Utils.entropia(probabilidadesCombinadas))
extension, probabilidadesCombinadas = ej10.generarConExtension(alfabeto, probabilidades, 3)
print("H(S_3) =", Utils.entropia(probabilidadesCombinadas))