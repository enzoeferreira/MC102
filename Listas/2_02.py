"""
Faça um programa que leia um número n. Após isso, o seu programa deve ler uma
sequência de n números e imprimir uma mensagem indicando se a sequência lida está
ordenada de forma crescente ou não.
"""

n = int(input("Quantos números serão digitados? "))
i = 0
listas = []
crescente = True

while i < n:
    listas.append(int(input("Digite um número: ")))
    i += 1

i = 0

listasCresc = listas.copy()
listasCresc.sort()

while i < len(listas):
    if listas[i] == listasCresc[i]:
        i += 1
    else:
        crescente = False
        break
        
if crescente == True:
    print("Está em ordem crescente")
else:
    print("Não está em ordem crescente")
