import math
import os
import random
import re
import sys
import numpy as np
import pandas as pd

def play_dots_and_boxes():
    tablero = [[0 for _ in range(3)] for _ in range(3)]
    
    puntos_jugador1 = 0
    puntos_jugador2 = 0
    jugador = 1
    
    lista = []

    while True:
        print("La cuadricula actual es: ")
        for fila in tablero:
            print(fila)
        print("Jugador 1:", puntos_jugador1, "Jugador 2:", puntos_jugador2)
        if jugador == 1:
            print("Turno del jugador 1")
        else:
            print("Turno del jugador 2")
        x1, y1, x2, y2 = input("Meter las coordenadas (x1 y1 x2 y2): ").split()
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            if tablero[x1][y1] != 0 or tablero[x2][y2] != 0:
                print("La caja ya esta completada")
                continue
            tablero[x1][y1] = jugador
            tablero[x2][y2] = jugador
            lista.append((x1, y1, x2, y2))
            if jugador == 1:
                player1_score += 1
            else:
                player2_score += 1
        elif y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            if tablero[x1][y1] != 0 or tablero[x2][y2] != 0:
                print("La caja ya esta completada")
                continue
            tablero[x1][y1] = jugador
            tablero[x2][y2] = jugador
            lista.append((x1, y1, x2, y2))
            if jugador == 1:
                puntos_jugador1 += 1
            else:
                puntos_jugador2 += 1
        else:
            print("Coordenadas invalidas")
            continue
        if jugador == 1:
            jugador = 2
        else:
            jugador = 1
        if not any(0 in sublist for sublist in tablero):
            print("Game Over")
            print("Jugador 1:", puntos_jugador1, "Jugador 2:", puntos_jugador2)
            break


if __name__ == '__main__':
    play_dots_and_boxes()