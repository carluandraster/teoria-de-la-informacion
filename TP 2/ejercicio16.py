import ejercicio14 as ej14
import ejercicio15 as ej15

# Constantes
CADENA_A = "CAAACCAABAACBBCABACCAAABCBBACC"
CADENA_B = "BBAAACCAAABCCCAACCCBBACCAABBAA"

# Funciones
def resolver_inciso(cadena: str) -> None:
    alfabeto, matriz_de_transiciones = ej15.obtenerAlfabetoYTransiciones(cadena)
    if ej15.esFuenteDeMemoriaNula(matriz_de_transiciones):
        print("La cadena es fuente de memoria nula.")
    else:
        print("La cadena no es fuente de memoria nula.")
    print("Entropía de la fuente: ", ej14.entropiaMarkoviana(matriz_de_transiciones), " bits")

# Programa principal
print("Inciso A:")
resolver_inciso(CADENA_A)
print("\nInciso B:")
resolver_inciso(CADENA_B)