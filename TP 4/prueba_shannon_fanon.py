from Utils import shannon_fano

PROBABILIDADES = [0.2, 0.27, 0.4, 0.13]

codigos_shannon_fano = shannon_fano(PROBABILIDADES)
print("Códigos de Shannon-Fano:", codigos_shannon_fano)
# Salida esperada: ['001', '01', '1', '000']