import math
import os
import random
import re
import sys
import numpy as np
import pandas as pd

def cadena(cadena: str):
    texto = cadena.split(" ")
    texto.sort(key=lambda x: int(re.search(r'\d+', x).group()))

    print(texto)



if __name__ == '__main__':
    cadena = input("Introduce una cadena: ")
    cadena(cadena)


