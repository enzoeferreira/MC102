n = int(input("Digite um número: "))
i = 1

print(f"Os divisores de {n} são:")
while i <= n:
    if n % i == 0:
        print(i)
    i += 1