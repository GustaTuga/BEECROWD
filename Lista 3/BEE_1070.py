# Entrada de dados

x = int(input())

# Declaração de valores
cont = 1

# Processamento de dados

while cont <= 6:
    if x % 2 != 0:
        print(x)
        cont += 1
    x += 1

