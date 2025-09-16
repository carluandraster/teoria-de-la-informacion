import ejercicio9 as ej9

# Códigos del ejercicio 7
ej7_codigo1  = ["011", "000", "010", "101", "001", "100"]
ej7_codigo2  = ["110", "100", "101", "001", "110", "010"]
ej7_codigo3  = ["10", "1100", "0101", "1011", "0", "110"]
ej7_codigo4  = ["1101", "10", "1111", "1100", "1110", "0"]
ej7_codigo5  = ["011", "0111", "01", "0", "011111", "01111"]
ej7_codigo6  = ["1110", "0", "110", "1101", "1011", "10"]

# Códigos del ejercicio 8
ej8_codigo1  = ["==", "<", "<=", ">", ">=", "<>"]
ej8_codigo2  = [")", "[]", "]]", "([", "[()]", "([)]"]
ej8_codigo3  = ["/", "*", "-", "*", "++", "+-"]
ej8_codigo4  = [".,", ";", ",,", ":", "...", ",:;"]

print("Códigos del ejercicio 7:")
print("Código 1:", ej9.sumatoria_de_kraft(ej7_codigo1))
print("Código 2:", ej9.sumatoria_de_kraft(ej7_codigo2))
print("Código 3:", ej9.sumatoria_de_kraft(ej7_codigo3))
print("Código 4:", ej9.sumatoria_de_kraft(ej7_codigo4))
print("Código 5:", ej9.sumatoria_de_kraft(ej7_codigo5))
print("Código 6:", ej9.sumatoria_de_kraft(ej7_codigo6))

print("\nCódigos del ejercicio 8:")
print("Código 1:", ej9.sumatoria_de_kraft(ej8_codigo1))
print("Código 2:", ej9.sumatoria_de_kraft(ej8_codigo2))
print("Código 3:", ej9.sumatoria_de_kraft(ej8_codigo3))
print("Código 4:", ej9.sumatoria_de_kraft(ej8_codigo4))