# -*- coding: utf-8 -*-

# Universidade Federal do Acre
# Disciplina: LP1
# Gustavo Bezerra de Souza

def calcular_valor(codigo, quantidade):
    if codigo == 1:
        return quantidade * 4.00
    elif codigo == 2:
        return quantidade * 4.50
    elif codigo == 3:
        return quantidade * 5.00
    elif codigo == 4:
        return quantidade * 2.00
    elif codigo == 5:
        return quantidade * 1.50
    else:
        return "Código inválido"

# Entrada de dados
x, y = map(int, input().split())

# Processamento e saída de dados
valor_a_pagar = calcular_valor(x, y)

if isinstance(valor_a_pagar, str):
    print(valor_a_pagar)
else:
    print(f"Total: R$ {valor_a_pagar:.2f}")
