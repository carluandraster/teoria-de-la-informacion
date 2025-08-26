import random
# Hace una simulacion de Monte Carlo
def monte_carlo(alfabeto: list, probabilidades_acumuladas: list, n: int):
    simulacion = []
    for _ in range(n):
        r = random.random()
        for i, p_acum in enumerate(probabilidades_acumuladas):
            if r <= p_acum:
                simulacion.append(alfabeto[i])
                break
    return simulacion

# Main
cadena = "Hola, ¿cómo estás?"
alfabeto = []
frecuencias = []
for c in cadena:
    if c not in alfabeto:
        alfabeto.append(c)
        frecuencias.append(1)
    else:
        frecuencias[alfabeto.index(c)] += 1
print("a) ",alfabeto)
probabilidades = [f/len(cadena) for f in frecuencias]
print(probabilidades)
probabilidades_acumuladas = [sum(probabilidades[:i+1]) for i in range(len(probabilidades))]
print("b) ",''.join(monte_carlo(alfabeto, probabilidades_acumuladas, 10)))