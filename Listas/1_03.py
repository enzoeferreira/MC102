"""
Faça um programa que leia um número ponto flutuante x
e calcule o valor de
f(x) = raiz(x) + x/2 + x^x
"""

x = float(input("Digite um valor para x: "))

resultado = (x ** (1/2)) + (x / 2) + (x ** x)

print(f"Resultado = {resultado}")