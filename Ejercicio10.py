import math
import os
import random
import re
import sys
import numpy as np
import pandas as pd

class potencia:

    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def verificar(self):
        if self.numero2 < 0:
            print("nil")  
        else:
            resultado = 1
            for i in range(self.numero2):
                resultado = resultado * self.numero1
            print(resultado)
            

if __name__ == '__main__':
    numero1 = int(input("Introduce un numero: "))
    numero2 = int(input("Introduce un numero: "))
    potencia(numero1, numero2).verificar()