# declaração de valores
par = 0
impa = 0
num_positivo = 0
num_negativo = 0

# Entrada e processamento de dados

for i in range(5):
    n = int(input())
    if n % 2 == 0:
        par += 1
    else:
        impa += 1
    
    if n < 0:
        num_negativo += 1
    else:
        if n > 0:
            num_positivo += 1

# Saída de dados

print(f"{par} valor(es) par(es)")
print(f"{impa} valor(es) impar(es)")
print(f"{num_positivo} valor(es) positivo(s)")
print(f"{num_negativo} valor(es) negativo(s)")