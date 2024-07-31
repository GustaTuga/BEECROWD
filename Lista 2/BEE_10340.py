# -*- coding: utf-8 -*-
# Universidade Federal do Acre
# Gustavo Bezerra de Souza

def calcular_media_pesada(notas, pesos):
    soma = sum(nota * peso for nota, peso in zip(notas, pesos))
    soma_pesos = sum(pesos)
    return soma / soma_pesos

# Pesos para as notas
pesos = [2, 3, 4, 1]

# Entrada de dados
notas = list(map(float, input().split()))

# Verifica se a entrada está correta
if len(notas) != 4:
    raise ValueError("É necessário inserir exatamente 4 notas.")

# Calcula a média ponderada
media = calcular_media_pesada(notas, pesos)

# Exibe a média
print(f"Media: {media:.1f}")

# Verifica a situação do aluno
if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    # Entrada da nota do exame
    nota_exame = float(input())
    print(f"Nota do exame: {nota_exame:.1f}")
    
    # Calcula a nova média com o exame
    media_final = (media + nota_exame) / 2
    
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    
    # Exibe a média final
    print(f"Media final: {media_final:.1f}")
