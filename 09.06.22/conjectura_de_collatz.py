n = int(input("Digite um número inteiro: "))

while n != 1:
    if n % 2 == 0:
        sucessor = n / 2
    else:
        sucessor = (3 * n) + 1
    print(sucessor)
    n = sucessor
    