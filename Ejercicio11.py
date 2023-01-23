import math
import os
import random
import re
import sys
import numpy as np
import pandas as pd

class potencia4:

    def __init__(self, numero):
        self.numero = numero

    def potencia(self):
        while self.numero % 4 == 0:
            self.numero = self.numero / 4
            print(self.numero)

        if self.numero == 1:
            print("True")
        elif  self.numero == float(self.numero):
            print("False")
        else:
            print("False")

if __name__ == '__main__':
    numero = int(input("Introduce un numero: "))
    potencia4(numero).potencia()
