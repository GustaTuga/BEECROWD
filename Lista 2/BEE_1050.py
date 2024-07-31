# -*- coding: utf-8 -*-
# Universidade Federal do Acre
# Disciplina: Linguagem de Programação 1
# Gustavo Bezerra de Souza

# Códigos DDD e suas cidades correspondentes
ddd_cidades = {
    61: "Brasilia",
    71: "Salvador",
    11: "Sao Paulo",
    21: "Rio de Janeiro",
    32: "Juiz de Fora",
    19: "Campinas",
    27: "Vitoria",
    31: "Belo Horizonte"
}

# Leitura do código DDD
codigo_ddd = int(input())

# Verificação e impressão da cidade correspondente ou mensagem de erro
if codigo_ddd in ddd_cidades:
    print(ddd_cidades[codigo_ddd])
else:
    print("DDD nao cadastrado")
