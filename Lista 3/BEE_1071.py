# Leia dois valores inteiros X e Y
X = int(input())
Y = int(input())

# Garanta que X seja o menor número e Y seja o maior número
if X > Y:
    X, Y = Y, X

# Inicialize a soma
soma_impares = 0

# Itere através do intervalo e some os valores ímpares
for num in range(X + 1, Y):
    if num % 2 != 0:
        soma_impares += num

# Imprima o resultado
print(soma_impares)
