import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import ejercicio14 as ej14
from Matriz import Matriz

print("Inciso a)")
M = Matriz([[0.5, 1/3, 0],
            [0.5, 1/3, 1],
            [0,   1/3, 0]])
print(M)

print("Inciso b)")
print(ej14.estadosEstables(M))

print("Inciso c)")
print(ej14.entropiaMarkoviana(M), " bits")