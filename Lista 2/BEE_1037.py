# -*- coding: utf-8 -*-

# Universidade Federal do Acre
# Disciplina: LP1
# Gustavo Bezerra de Souza

# Função para determinar o intervalo
def determinar_intervalo(numero):
    if 0 <= numero <= 25:
        return "Intervalo [0,25]"
    elif 25 < numero <= 50:
        return "Intervalo (25,50]"
    elif 50 < numero <= 75:
        return "Intervalo (50,75]"
    elif 75 < numero <= 100:
        return "Intervalo (75,100]"
    else:
        return "Fora de intervalo"

# Entrada de dados
numero = float(map(float, input().split()).__next__())

# Processamento e saída de dados
resultado = determinar_intervalo(numero)
print(resultado)
