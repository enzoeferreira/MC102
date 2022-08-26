"""
Faça um programa que leia um ano (valor inteiro) e imprima se ele é bissexto ou não.
Observação: um ano é bissexto se ele é múltiplo de 400, ou se ele é múltiplo de 4 mas não
é múltiplo de 100.
"""

ano = int(input("Digite o ano: "))

if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    print("\nO ano e bissexto")
else:
    print("\nO ano nao e bissexto")