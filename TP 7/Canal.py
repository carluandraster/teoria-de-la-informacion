from Matriz import Matriz
import MatrizFactory as mf
from Utils import entropia
from math import log2, isclose

class Canal:
    """Clase que representa un canal de comunicación con su matriz de transición y probabilidades a priori.
    
    Constructor:
    ------------
    :param Matriz[float] matriz_canal: Matriz de canal que representa las probabilidades de transición.
    :param list[float] probs_a_priori: Lista de probabilidades a priori para los símbolos de entrada. Si es None, se asignan probabilidades uniformes.
    
    Métodos:
    --------
    - get_probabilidades_salidas(): Calcula las probabilidades de las salidas del canal.
    - get_probabilidades_a_posteriori(): Calcula la matriz de probabilidades a posteriori P(A/B).
    - get_probabilidades_eventos_simultaneos(): Calcula la matriz de probabilidades P(A,B).
    - entropia_a_posteriori(): Calcula la entropía a posteriori para cada símbolo recibido.
    - get_ruido(): Calcula el ruido del canal de comunicación.
    - get_perdida(): Calcula la pérdida del canal de comunicación.
    - get_entropia_afin(): Calcula la entropía afín del canal de comunicación.
    - get_informacion_mutua(): Calcula la información mutua del canal de comunicación
    """
    __matriz_canal: Matriz[float]
    __probs_a_priori: list[float]
    
    def __init__(self, matriz_canal: Matriz[float], probs_a_priori: list[float] = []) -> None:
        """Constructor de la clase Canal.
        
        :param Matriz[float] matriz_canal: Matriz de canal que representa las probabilidades de transición.
        :param list[float] probs_a_priori: Lista de probabilidades a priori para los símbolos de entrada. Si es None, se asignan probabilidades uniformes.
        
        :raises ValueError: Si las filas de la matriz de canal no suman 1 o si las probabilidades a priori no son válidas.
        
        Pre: la matriz contiene, al menos, una fila y una columna.
        """
        self.__matriz_canal = matriz_canal
        for i in range(matriz_canal.cantidadFilas):
            if not isclose(sum(self.__matriz_canal.getFila(i)), 1.0, rel_tol=1e-9):
                raise ValueError(f"La fila {i} de la matriz de canal no suma 1.")
        if not probs_a_priori:
            self.__probs_a_priori = [1.0 / matriz_canal.cantidadFilas] * matriz_canal.cantidadFilas
        else:
            if len(probs_a_priori) != matriz_canal.cantidadFilas:
                raise ValueError("La longitud de las probabilidades a priori debe coincidir con el número de filas de la matriz de canal.")
            elif not isclose(sum(probs_a_priori), 1.0, rel_tol=1e-9):
                raise ValueError("La suma de las probabilidades a priori debe ser 1.")
            else:
                self.__probs_a_priori = probs_a_priori
    
    @property
    def get_matriz_canal(self) -> Matriz[float]:
        """Devuelve la matriz de canal del objeto Canal."""
        return self.__matriz_canal
    
    @property
    def get_probs_a_priori(self) -> list[float]:
        """Devuelve las probabilidades a priori del objeto Canal."""
        return self.__probs_a_priori
    
    def set_matriz_canal(self, matriz_canal: Matriz[float]) -> None:
        """Establece la matriz de canal del objeto Canal.
        
        :param Matriz[float] matriz_canal: Nueva matriz de canal.
        :raises ValueError: Si alguna fila de la matriz no suma 1.
        Pre: la matriz contiene, al menos, una fila y una columna.
        """
        for i in range(matriz_canal.cantidadFilas):
            if not isclose(sum(matriz_canal.getFila(i)), 1.0, rel_tol=1e-9):
                raise ValueError(f"La fila {i} de la matriz de canal no suma 1.")
        self.__matriz_canal = matriz_canal
    
    def set_probs_a_priori(self, probs_a_priori: list[float]) -> None:
        """Establece las probabilidades a priori del objeto Canal."""
        if len(probs_a_priori) != self.__matriz_canal.cantidadFilas:
            raise ValueError("La longitud de las probabilidades a priori debe coincidir con el número de filas de la matriz de canal.")
        elif not isclose(sum(probs_a_priori), 1.0, rel_tol=1e-9):
            raise ValueError("La suma de las probabilidades a priori debe ser 1.")
        self.__probs_a_priori = probs_a_priori

    
    def get_probabilidades_salidas(self) -> list[float]:
        """
        Calcula P(B); es decir, las probabilidades de las salidas del canal de comunicación.

        :return: Lista de probabilidades de las salidas.
        """
        # Convertir la lista de probabilidades a priori en una matriz columna
        matriz_entradas = Matriz([self.__probs_a_priori])
        
        # Calcular la matriz de probabilidades de salidas
        matriz_salidas = matriz_entradas * self.__matriz_canal

        # Devolver la lista de probabilidades de las salidas
        return matriz_salidas[0]

    def get_probabilidades_a_posteriori(self) -> Matriz[float]:
        """
        Calcula la matriz de probabilidades P(A/B) que respresenta las probabilidades
        a posteriori de las entradas dado el canal de comunicación.

        :return: Matriz de probabilidades a posteriori, donde cada elemento (i, j)
        representa la probabilidad de que la entrada i haya ocurrido dado que se observó la salida j.
        """
        # Obtener las probabilidades de las salidas
        probabilidades_salidas = self.get_probabilidades_salidas()

        # Crear una matriz para las probabilidades a posteriori
        matriz_a_posteriori = mf.ceros(self.__matriz_canal.cantidadFilas, self.__matriz_canal.cantidadColumnas)

        # Calcular las probabilidades a posteriori usando el teorema de Bayes
        for i in range(self.__matriz_canal.cantidadFilas):
            for j in range(self.__matriz_canal.cantidadColumnas):
                if probabilidades_salidas[j] != 0:
                    matriz_a_posteriori[i][j] = (self.__matriz_canal[i][j] * self.__probs_a_priori[i]) / probabilidades_salidas[j]
                else:
                    matriz_a_posteriori[i][j] = 0.0

        return matriz_a_posteriori

    def get_probabilidades_eventos_simultaneos(self) -> Matriz[float]:
        """
        Calcula la matriz de probabilidades P(A,B); es decir, las probabilidades de eventos simultáneos
        de entradas y salidas en un canal de comunicación.

        :return: Matriz de probabilidades de eventos simultáneos, donde cada elemento (i, j)
        representa la probabilidad de que ocurra la entrada i y se observe la salida j.
        """
        # Crear una matriz para las probabilidades de eventos simultáneos
        matriz_eventos_simultaneos = mf.ceros(self.__matriz_canal.cantidadFilas, self.__matriz_canal.cantidadColumnas)

        # Calcular las probabilidades de eventos simultáneos
        for i in range(self.__matriz_canal.cantidadFilas):
            for j in range(self.__matriz_canal.cantidadColumnas):
                matriz_eventos_simultaneos[i][j] = self.__matriz_canal[i][j] * self.__probs_a_priori[i]

        return matriz_eventos_simultaneos
    
    def entropia_a_posteriori(self) -> list[float]:
        """Calcula la entropía a posteriori para cada símbolo recibido.

        :return: list[float]: Entropías a posteriori para cada símbolo recibido.
        """
        probabilidades_a_posteriori = self.get_probabilidades_a_posteriori()
        entropias: list[float] = []
        N = probabilidades_a_posteriori.cantidadColumnas
        for i in range(N):
            entropias.append(entropia(probabilidades_a_posteriori.getColumna(i)))
        return entropias
    
    def get_ruido(self)->float:
        """Calcula el ruido de un canal de comunicacion.

        Returns:
            float: Ruido del canal.
        """
        probs_salidas = self.get_probabilidades_salidas()
        H_A_given_b = self.entropia_a_posteriori()
        H_A_given_B = 0
        for p, h in zip(probs_salidas, H_A_given_b):
            H_A_given_B += p * h
        return H_A_given_B

    def get_perdida(self)->float:
        """Calcula la perdida de un canal de comunicacion.

        Returns:
            float: Perdida del canal.
        """
        H_A_given_B = self.get_ruido()
        H_A = entropia(self.__probs_a_priori)
        H_B = entropia(self.get_probabilidades_salidas())
        return H_A_given_B + H_B - H_A

    def get_entropia_afin(self)->float:
        """Calcula la entropia afin de un canal de comunicacion.

        Returns:
            float: Entropia afin del canal.
        """
        P_a_b = self.get_probabilidades_eventos_simultaneos()
        entropia_afin = 0
        for fila in P_a_b:
            entropia_afin += entropia(fila)
        return entropia_afin

    def get_informacion_mutua(self)->float:
        """Calcula la informacion mutua de un canal de comunicacion.

        Returns:
            float: Informacion mutua del canal.
        """
        P = self.get_probabilidades_eventos_simultaneos()
        informacion_mutua = 0
        probs_salidas = self.get_probabilidades_salidas()
        for a in range(len(self.__probs_a_priori)):
            for b in range(len(probs_salidas)):
                if(P[a][b] > 0):
                    informacion_mutua += P[a][b] * log2(P[a][b] / (self.__probs_a_priori[a] * probs_salidas[b]))
        return informacion_mutua