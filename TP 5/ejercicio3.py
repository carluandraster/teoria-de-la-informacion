from Canal import Canal

CANAL1 = Canal("1101011001101010010101010100011111", "1001111111100011101101010111110110")
CANAL2 = Canal("110101100110101100110101100111110011", "110021102110022010220121122100112011")

def resolver(nombre: str, canal: Canal) -> None:
    print(nombre)
    print("Probabilidades a priori: \n", canal.get_probabilidades_a_priori())
    print("Matriz del canal: \n", canal.get_matriz_del_canal())
    print("--------------------------\n")

resolver("Canal 1", CANAL1)
resolver("Canal 2", CANAL2)