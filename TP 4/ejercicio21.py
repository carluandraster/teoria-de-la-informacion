from ejercicio22 import get_distancia_de_hamming

CODIGO1 = ["00", "01", "10", "11"]
CODIGO2 = ["000", "100", "101", "111"]
CODIGO3 = ["0000", "0011", "1010", "0101"]

print("\t\tCodigo 1\tCodigo 2\tCodigo 3")
distancia_de_haming1, detectables1, correctibles1 = get_distancia_de_hamming(CODIGO1)
distancia_de_haming2, detectables2, correctibles2 = get_distancia_de_hamming(CODIGO2)
distancia_de_haming3, detectables3, correctibles3 = get_distancia_de_hamming(CODIGO3)
print("Distancia minima:\t", distancia_de_haming1, "\t\t", distancia_de_haming2, "\t\t", distancia_de_haming3)
print("Capacidad de correccion:\t", correctibles1, "\t\t", correctibles2, "\t\t", correctibles3)
print("Capacidad de deteccion:\t", detectables1, "\t\t", detectables2, "\t\t", detectables3)