# -*- coding: utf-8 -*-
# Universidade Federal do Acre
# Disciplina: Linguagem de Programação 1
# Gustavo Bezerra de Souza

# Função para calcular a duração do jogo
def calcular_duracao_jogo(inicio, termino):
    if termino <= inicio:
        duracao = 24 - inicio + termino
    else:
        duracao = termino - inicio

    print(f"O JOGO DUROU {duracao} HORA(S)")

# Entrada de dados
inicio, termino = map(int, input().split())

# Processamento e saída de dados
calcular_duracao_jogo(inicio, termino)
