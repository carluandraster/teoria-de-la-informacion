from algebra_lineal.Matriz import Matriz
import algebra_lineal.MatrizFactory as mf
from Utils import get_informacion_mutua
from ejercicio2 import es_canal_determinante
from ejercicio7 import reducir_matriz

A_1 = [1/3] * 3
A_2 = [1/3] * 3
A_3 = [1/3] * 3
A_4 = [1/4] * 4

def resolver(titulo, probs_a_priori, matriz_canal: Matriz[float]):
    print(f"---{titulo}---")
    print("I(A,B) = ", get_informacion_mutua(probs_a_priori, matriz_canal))
    post_producto = mf.identidad(matriz_canal.cantidadColumnas - 1)
    post_producto.insertar_fila(1, [1, 0, 0])
    matriz_canal *= post_producto
    print("Canal modificado:\n", matriz_canal)
    print("I(A,B) = ", get_informacion_mutua(probs_a_priori, matriz_canal))
    if es_canal_determinante(matriz_canal):
        print("El canal es determinante después de la modificación.")
    else:
        print("El canal no es determinante después de la modificación.")

if __name__ == "__main__":
    canal_1 = Matriz([
        [0.4, 0.6, 0.0, 0.0],
        [0.0, 0.0, 0.5, 0.5],
        [0.0, 0.0, 0.7, 0.3]
    ])
    canal_2 = Matriz([
        [0.2, 0.3, 0.5],
        [0.0, 0.0, 1.0],
        [0.0, 0.0, 1.0]
    ])
    canal_3 = Matriz([
        [0.4, 0.0, 0.2, 0.4],
        [0.4, 0.3, 0.2, 0.1],
        [0.0, 0.3, 0.0, 0.7]
    ])
    canal_4 = Matriz([
        [0.0, 0.5, 0.0, 0.5],
        [0.8, 0.0, 0.2, 0.0],
        [0.0, 0.5, 0.0, 0.5],
        [0.8, 0.0, 0.2, 0.0]
    ])

    resolver("---Canal 1---", A_1, canal_1)

    # print("\n---Canal 2---")
    # print("I(A,B) = ", get_informacion_mutua(A_2, canal_2))
    # post_producto = mf.identidad(canal_2.cantidadColumnas - 1)
    # post_producto.insertar_fila(1, [1, 0])
    # canal_2 *= post_producto
    # print("Canal modificado:\n", canal_2)
    # print("I(A,B) = ", get_informacion_mutua(A_2, canal_2))
    # if es_canal_determinante(canal_2):
    #     print("El canal es determinante después de la modificación.")
    # else:
    #     print("El canal no es determinante después de la modificación.")

    # print("\n---Canal 3---")
    # print("I(A,B) = ", get_informacion_mutua(A_3, canal_3))
    # post_producto = mf.identidad(canal_3.cantidadColumnas - 1)
    # post_producto.insertar_fila(2, [1, 0, 0])
    # canal_3 *= post_producto
    # print("Canal modificado:\n", canal_3)
    # print("I(A,B) = ", get_informacion_mutua(A_3, canal_3))
    # if es_canal_determinante(canal_3):
    #     print("El canal es determinante después de la modificación.")
    # else:
    #     print("El canal no es determinante después de la modificación.")
    
    # print("\n---Canal 4---")
    # print("I(A,B) = ", get_informacion_mutua(A_4, canal_4))
    # post_producto = mf.identidad(canal_4.cantidadColumnas - 1)
    # post_producto.insertar_fila(2, [1, 0, 0])
    # canal_4 *= post_producto
    # print("Canal modificado:\n", canal_4)
    # print("I(A,B) = ", get_informacion_mutua(A_4, canal_4))
    # post_producto = mf.identidad(canal_4.cantidadColumnas - 1)
    # post_producto.agregarFila([0, 1])
    # canal_4 *= post_producto
    # print("Canal modificado:\n", canal_4)
    # print("I(A,B) = ", get_informacion_mutua(A_4, canal_4))
    # if es_canal_determinante(canal_4):
    #     print("El canal es determinante después de la modificación.")
    # else:
    #     print("El canal no es determinante después de la modificación.")