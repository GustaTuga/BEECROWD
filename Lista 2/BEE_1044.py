# -*- coding: utf-8 -*-
# Universidade Federal do Acre
# disciplina: Linguagem de Programação 1
# Gustavo Bezerra de Souza

# Função para verificar se os números são múltiplos
def verificar_multiplos(A, B):
    if A % B == 0 or B % A == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")

# Entrada de dados
A, B = map(int, input().split())

# Processamento e saída de dados
verificar_multiplos(A, B)
