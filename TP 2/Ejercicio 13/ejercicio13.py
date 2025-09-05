import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import Utils
from Matriz import Matriz

M = Matriz(3,3, [[0.5, 1/3, 0],
                 [0.5, 1/3, 1],
                 [0,   1/3, 0]])
print(Utils.estadosEstables(M))