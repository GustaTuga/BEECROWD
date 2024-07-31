# -*- coding: utf-8 -*-

# Universidade Federal do Acre
# Disciplina: Linguagem de Programação 1
# Gustavo Bezerra de Souza

# Função para determinar a localização do ponto
def determinar_localizacao(x, y):
    if x == 0 and y == 0:
        return "Origem"
    elif x == 0:
        return "Eixo Y"
    elif y == 0:
        return "Eixo X"
    elif x > 0 and y > 0:
        return "Q1"
    elif x < 0 and y > 0:
        return "Q2"
    elif x < 0 and y < 0:
        return "Q3"
    elif x > 0 and y < 0:
        return "Q4"

# Entrada de dados
x, y = map(float, input().split())

# Processamento e saída de dados
localizacao = determinar_localizacao(x, y)
print(localizacao)
