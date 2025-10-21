from ejercicio2 import get_matriz_del_canal
from Utils import get_frecuencias

class Canal:
    __entrada: str
    __salida: str

    def __init__(self, entrada: str, salida: str):
        self.__entrada = entrada
        self.__salida = salida
    
    @property
    def entrada(self) -> str:
        return self.__entrada
    
    @property
    def salida(self) -> str:
        return self.__salida
    
    @property
    def entrada(self, entrada: str):
        self.__entrada = entrada
    
    @property
    def salida(self, salida: str):
        self.__salida = salida

    def get_matriz_del_canal(self):
        return get_matriz_del_canal(self.__entrada, self.__salida)
    
    def get_probabilidades_a_priori(self):
        return get_frecuencias(self.__entrada)