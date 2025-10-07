from ejercicio1 import primer_teorema_shannon

C1 = ["11", "010", "00"]
P = [0.5, 0.2, 0.3]

if(primer_teorema_shannon(P, C1, 1)):
    print("El código C1 cumple el primer teorema de Shannon")
else:
    print("El código C1 no cumple el primer teorema de Shannon")

if(primer_teorema_shannon(P, C1, 2)):
    print("La extension 2 del código C1 cumple el primer teorema de Shannon")
else:
    print("La extension 2 del código C1 no cumple el primer teorema de Shannon")