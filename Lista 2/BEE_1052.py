# -*- coding: utf-8 -*-
# Universidade Federal do Acre
# Disciplina: Linguagem de Programação
# Gustavo Bezerra de Souza

# números dos meses e seus nomes correspondentes
meses = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

# Leitura do número do mês
numero_mes = int(input())

# Verificação e impressão do mês correspondente
if 1 <= numero_mes <= 12:
    print(meses[numero_mes])
else:
    print("Número do mês inválido")
