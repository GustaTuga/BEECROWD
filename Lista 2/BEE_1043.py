# -*- coding: utf-8 -*-
# Universidade Federal do Acre
# Disciplina: Linguagem de Programação 1
# Gustavo Bezerra de Souza

# Função para ordenar e imprimir os valores
def ordenar_e_imprimir(valores):
    # Ordena os valores
    valores_ordenados = sorted(valores)
    
    # Imprime os valores em ordem crescente, cada um em uma nova linha
    for valor in valores_ordenados:
        print(valor)
    
    # Imprime uma linha em branco
    print()
    
    # Imprime os valores na ordem original, cada um em uma nova linha
    for valor in valores:
        print(valor)

# Entrada de dados
valores = list(map(int, input().split()))

# Verifica se foram lidos exatamente 3 valores
if len(valores) != 3:
    raise ValueError("É necessário inserir 3 números inteiros.")

# Processamento e saída de dados
ordenar_e_imprimir(valores)
