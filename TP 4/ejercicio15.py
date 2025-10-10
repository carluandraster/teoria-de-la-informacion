class Decodificador:
    """Clase que permite decodificar mensajes codificados o codificar mensajes
    utilizando un alfabeto fuente y una codificacion dada.
    
    Métodos:
        - decodificar(mensaje_codificado: str) -> str: Decodifica un mensaje codificado.
        - codificar(mensaje: str) -> str: Codifica un mensaje utilizando la codificacion dada.
    """
    __alfabeto_fuente: str
    __codificacion: list[str]

    def __init__(self, alfabeto_fuente: str, codificacion: list[str]):
        """Constructor de la clase Decodificador.
        
        Parametros:
            - alfabeto_fuente: lista de simbolos del alfabeto fuente.
            - codificacion: lista de codigos correspondientes a cada simbolo del alfabeto fuente.
        
        Precondiciones:
            - len(alfabeto_fuente) == len(codificacion)
            - Todos los elementos de alfabeto_fuente son distintos.
            - Tanto alfabeto_fuente como codificacion no estan vacios y son distintos de None.
            - La codificacion es binaria (solo contiene '0' y '1').
        """
        self.__alfabeto_fuente = alfabeto_fuente
        self.__codificacion = codificacion

    def decodificar(self, mensaje_codificado: bytearray) -> str:
        """Decodifica un mensaje codificado utilizando la codificacion dada.
        
        Parametros:
            - mensaje_codificado: mensaje codificado a decodificar.
            
        Retorna: mensaje decodificado.
        
        Arroja ValueError si el mensaje no se puede decodificar completamente.
        
        Precoindiciones:
            - mensaje_codificado no es None ni una cadena vacia.
        """
        mensaje_decodificado = ""
        aux = ""
        for byte in mensaje_codificado:
            bits = format(byte, '08b')  # Convertir byte a una cadena de 8 unos y ceros
            for bit in bits:
                aux += bit
                if aux in self.__codificacion:
                    mensaje_decodificado += self.__alfabeto_fuente[self.__codificacion.index(aux)]
                    aux = ""
        if aux != "":
            raise ValueError("El mensaje no se pudo decodificar completamente.")
        return mensaje_decodificado
    
    def codificar(self, mensaje: str) -> bytearray:
        """Codifica un mensaje utilizando la codificacion dada.
        
        Parametros:
            - mensaje: mensaje a codificar.
        
        Retorna: mensaje codificado.
        
        Arroja ValueError si el mensaje contiene simbolos que no estan en el alfabeto fuente.
        
        Precondiciones:
            - mensaje no es None ni una cadena vacia.
        """
        mensaje_codificado = bytearray()
        aux = ""
        for simbolo in mensaje:
            if simbolo in self.__alfabeto_fuente:
                aux += self.__codificacion[self.__alfabeto_fuente.index(simbolo)]
            else:
                raise ValueError(f"El símbolo '{simbolo}' no está en el alfabeto fuente.")
        for i in range(0, len(aux), 8):
            byte = aux[i:i+8]
            mensaje_codificado.append(int(byte, 2))
        return mensaje_codificado
