n = int(input("Digite um número inteiro: "))

print(f"Os divisores de {n} são:")
for i in range (1, n + 1):
    if n % i == 0:
        print(i)
