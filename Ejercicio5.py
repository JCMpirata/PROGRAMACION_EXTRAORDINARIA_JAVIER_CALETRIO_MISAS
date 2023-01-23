import math
import os
import random
import re
import sys
import numpy as np
import pandas as pd
import string

def decrypt_vigenere(cifrado, longitud_clave):
    coincidencias = []
    for i in range(1, longitud_clave+1):
        sum = 0
        for j in range(i, len(cifrado), i):
            sum += (cifrado.count(cifrado[j]) * (cifrado.count(cifrado[j])-1)) / (len(cifrado) * (len(cifrado)-1))
        coincidencias.append(sum)
    
    indice = max(coincidencias)
    key_length = coincidencias.index(indice) + 1
    
    blocks = [cifrado[i:i+key_length] for i in range(0, len(cifrado), key_length)]
    
   
    key = ""
    for block in blocks:
        frequency = {}
        for letter in string.ascii_uppercase:
            frequency[letter] = block.count(letter) / len(block)
        most_frequent_letter = max(frequency, key=frequency.get)
        shift = ord(most_frequent_letter) - ord("E")
        key += chr((shift % 26) + ord("A"))
    
    return key

if __name__ == '__main__':
    cifrado = input()
    longitud_clave = int(input())
    print(decrypt_vigenere(cifrado, longitud_clave))