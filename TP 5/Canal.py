from ejercicio2 import get_matriz_del_canal
from Utils import get_frecuencias
from algebra_lineal.Matriz import Matriz

class Canal:
    """
    Clase que representa un canal de comunicacion con una entrada y una salida.

    Atributos:
    ----------
    - entrada : str
        La cadena de caracteres que representa la entrada del canal.
    - salida : str
        La cadena de caracteres que representa la salida del canal.
    
    Metodos:
    -------
    - get_matriz_del_canal() -> Matriz[float]:
        Devuelve la matriz de probabilidades condicionales del canal.
    - get_probabilidades_a_priori() -> dict[str, float]:
        Devuelve las probabilidades a priori de los simbolos en la entrada del canal.
    """
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

    def get_matriz_del_canal(self) -> Matriz[float]:
        """
        Devuelve la matriz de probabilidades condicionales del canal.

        :return: Matriz[float]
        """
        return get_matriz_del_canal(self.__entrada, self.__salida)
    
    def get_probabilidades_a_priori(self) -> dict[str, float]:
        """Devuelve las probabilidades a priori de los simbolos en la entrada del canal.
        
        :return: dict[str, float]"""
        return get_frecuencias(self.__entrada)