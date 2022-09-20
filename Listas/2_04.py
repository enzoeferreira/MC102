"""
Escreva um programa que leia um número n. O seu programa deve imprimir o menor
número primo que é maior ou igual n e o maior número primo que é menor ou igual a n.
"""

n = float(input("Digite um número: "))

primos = [2]

num = 3
i = 0
while primos[i] <= n:
    div = 2
    primo = True
    while div <= (num / 2) and primo == True:
        if num % div == 0:
            primo = False
        div += 1
    if primo == True:
        primos.append(num)
        i += 1
    num += 1

i = 0
for i in range(len(primos)):
    if i < len(primos):
        if primos[i] <= n and primos[i + 1] >= n:
            print(f"O maior primo MENOR OU IGUAL {n} é {primos[i]}\nO menor primo MAIOR OU IGUAL {n} é {primos[i + 1]}")