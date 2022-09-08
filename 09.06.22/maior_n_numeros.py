n = int(input("Quantos números serão digitados? "))

maior = 0
i = 0

while i < n:
    x = float(input("Digite um número: "))
    
    if x > maior:
        maior = x
    i += 1

print("Maior =", maior)