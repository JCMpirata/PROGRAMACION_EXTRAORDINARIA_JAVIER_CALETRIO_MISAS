import itertools

def word_number(word):
    # Generar todas las permutaciones de la palabra
    permutations = list(itertools.permutations(word))
    # Ordenar las permutaciones alfabéticamente
    permutations.sort()
    # Encontrar la posición de la palabra dada en la lista de permutaciones ordenadas
    position = permutations.index(tuple(word))
    # Devolver el número correspondiente a esa posición
    return position + 1

print(word_number("ABAB")) # 2
print(word_number("AAAB")) # 1
print(word_number("BAAA")) # 4
print(word_number("PREGUNTA")) # 24572
print(word_number("CONTADOR"))# 10743