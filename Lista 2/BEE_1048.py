# -*- coding: utf-8 -*-
# Universidade Federal do Acre
# Disciplina: Linguagem de Programação 1
# Gustavo Bezerra de Souza

def calcular_reajuste(salario):
    # Definir as taxas de reajuste e os limites das faixas salariais
    if salario <= 400.00:
        percentual = 15
    elif salario <= 800.00:
        percentual = 12
    elif salario <= 1200.00:
        percentual = 10
    elif salario <= 2000.00:
        percentual = 7
    else:
        percentual = 4
    
    # Calcular o aumento e o novo salário
    aumento = salario * percentual / 100
    novo_salario = salario + aumento
    
    # Imprimir os resultados
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {aumento:.2f}")
    print(f"Em percentual: {percentual} %")

# Entrada de dados
salario = float(input())

# Processamento e saída de dados
calcular_reajuste(salario)
