N = int(input())

for _ in range(N):
    num1, num2, num3 = map(float, input().split())
    
    media_ponderada = (num1 * 2 + num2 * 3 + num3 * 5) / 10
    
    print(f"{media_ponderada:.1f}")
