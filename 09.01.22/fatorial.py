a = int(input("Digite um número: "))
n = a - 1

fatorial = a

if a == 0:
    fatorial = 1
else:
    while n >= 1:
        fatorial = fatorial * n
        n -= 1

print(f"{a}! = {fatorial}")