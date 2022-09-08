n = int(input("Digite um número inteiro: "))

print(f"Divisores não triviais de {n}")
for i in range (2, n):
    if n % i == 0:
        print(i)