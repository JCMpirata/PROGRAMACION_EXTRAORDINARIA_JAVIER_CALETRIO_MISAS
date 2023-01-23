import math
import os
import random
import re
import sys
import numpy as np
import pandas as pd
import itertools

def word_number(word):
    permutations = list(itertools.permutations(word))
    permutations.sort()
    position = permutations.index(tuple(word))
    return position + 1

print(word_number("ABAB"))
print(word_number("AAAB")) 
print(word_number("BAAA")) 
print(word_number("PREGUNTA")) 
print(word_number("CONTADOR"))