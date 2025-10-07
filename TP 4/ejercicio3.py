from ejercicio1 import primer_teorema_shannon

C1 = ["11", "010", "00"]
C2 = ["10", "001", "110", "010", "0000", "0001", "111", "0110", "0111"]
P = [0.5, 0.2, 0.3]
P_2 = [P[i]*P[j] for i in range(len(P)) for j in range(len(P))]

if(primer_teorema_shannon(P, C1, 1)):
    print("El código C1 cumple el primer teorema de Shannon")
else:
    print("El código C1 no cumple el primer teorema de Shannon")

if(primer_teorema_shannon(P_2, C2, 2)):
    print("La extension 2 del código C1 cumple el primer teorema de Shannon")
else:
    print("La extension 2 del código C1 no cumple el primer teorema de Shannon")