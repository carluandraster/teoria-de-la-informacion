import Utils

codigo1  = ["==", "<", "<=", ">", ">=", "<>"]
codigo2  = [")", "[]", "]]", "([", "[()]", "([)]"]
codigo3  = ["/", "*", "-", "*", "++", "+-"]
codigo4  = [".,", ";", ",,", ":", "...", ",:;"]

print("Codigo 1:", Utils.clasificar(codigo1))
print("Codigo 2:", Utils.clasificar(codigo2))
print("Codigo 3:", Utils.clasificar(codigo3))
print("Codigo 4:", Utils.clasificar(codigo4))