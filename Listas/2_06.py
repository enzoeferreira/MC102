"""
Escreva um programa que leia n números inteiros e imprima quantos deles estão nos
seguintes intervalos: [0, 25], [26, 50], [51, 75] e [76, 100].

Por exemplo, para n = 10 e os seguintes números {2, 61, −1, 0, 88, 55, 3, 121, 25, 75},
seu programa deve imprimir:
[0 ,25]: 4
[26 ,50]: 0
[51 ,75]: 3
[76 ,100]: 1
"""

n = int(input("Quantos números serão digitados? "))

numeros = []

for _ in range(n):
    entrada = int(input("Digite um número: "))
    numeros.append(entrada)
    
int1 = 0
int2 = 0
int3 = 0
int4 = 0
for numero in numeros:
    if 0 <= numero <= 25:
        int1 += 1
    elif 26 <= numero <= 50:
        int2 += 1
    elif 51 <= numero <= 75:
        int3 += 1
    elif 76 <= numero <= 100:
        int4 += 1
        
print("[0, 25]:", int1)
print("[26, 50]:", int2)
print("[51, 75]:", int3)
print("[76, 100]:", int4)
    