# -*- coding: utf-8 -*-
# Universidade Federal do Acre
# Disciplina: Linguagem de Programação 1
# Gustavo Bezerra de Souza

def classificar_triangulo(A, B, C):
    # Ordenar os lados em ordem decrescente
    A, B, C = sorted([A, B, C], reverse=True)
    
    # Verificar se forma um triângulo
    if A >= B + C:
        print("NAO FORMA TRIANGULO")
    else:
        # Verificar o tipo de triângulo
        if A**2 == B**2 + C**2:
            print("TRIANGULO RETANGULO")
        elif A**2 > B**2 + C**2:
            print("TRIANGULO OBTUSANGULO")
        elif A**2 < B**2 + C**2:
            print("TRIANGULO ACUTANGULO")
        
        # Verificar se é equilátero ou isósceles
        if A == B == C:
            print("TRIANGULO EQUILATERO")
        elif A == B or B == C or A == C:
            print("TRIANGULO ISOSCELES")

# Entrada de dados
A, B, C = map(float, input().split())

# Processamento e saída de dados
classificar_triangulo(A, B, C)
