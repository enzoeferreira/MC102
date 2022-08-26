"""
Faça um programa que leia dois números e em seguida um caracter que representa um
operador aritmético (‘+’, ‘−’, ‘∗’ ou ‘/’). Seu programa então deve imprimir o resultado
do operador aplicado aos dois números dados.
"""
x = float(input("Digite o valor de X: "))
y = float(input("Digite o valor de Y: "))
operacao = input("Qual operacao? (+ , -, * ou /) ")
validade = 1

if operacao == '+':
    resultado = x + y
elif operacao == '-':
    resultado = x - y
elif operacao == '*':
    resultado = x * y
elif operacao == '/':
    resultado = x / y
else:
    print("\nOperacao nao encontrada.")
    validade = 0

if bool(validade):
    print(f"\nResultado = {resultado:.2f}")