# Leia o número de casos de teste N
N = int(input())

# Iterar pelos N valores inteiros
for _ in range(N):
    X = int(input())
    
    if X == 0:
        print("NULL")
    else:
        if X % 2 == 0:
            tipo = "EVEN"
        else:
            tipo = "ODD"
        
        if X > 0:
            sinal = "POSITIVE"
        else:
            sinal = "NEGATIVE"
        
        print(f"{tipo} {sinal}")
