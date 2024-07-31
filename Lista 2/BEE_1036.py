# -*- coding: utf-8 -*-
#Universidade Federal do Acre
#Disciplina: LP1
#Gustavo Bezerra de Souza

import math

def calcular_raizes(a, b, c):
    delta = b**2 - 4*a*c

    if a == 0 or delta < 0:
        return "Impossivel calcular"
    else:
        R1 = (-b + math.sqrt(delta)) / (2 * a)
        R2 = (-b - math.sqrt(delta)) / (2 * a)
        return f"R1 = {R1:.5f}\nR2 = {R2:.5f}"

# Entrada de dados
a, b, c = map(float, input().split())

# Processamento e saída de dados
resultado = calcular_raizes(a, b, c)
print(resultado)
