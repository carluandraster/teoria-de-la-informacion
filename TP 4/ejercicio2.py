import ejercicio1 as ej1

probs = [0.3, 0.1, 0.4, 0.2]
codigo = ["BA", "CAB", "A", "CBA"]
N = 2

if(ej1.primer_teorema_shannon(probs, codigo, N)):
    print("La extensión de orden 2 del código cumple con el primer teorema de Shannon.")
else:
    print("La extensión de orden 2 del código no cumple con el primer teorema de Shannon.")