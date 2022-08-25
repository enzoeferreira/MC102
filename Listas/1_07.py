"""
Faça um programa que leia um caractere ‘F’ ou ‘C’, que indica se o próximo valor
corresponde à temperatura em Fahrenheit ou Celsius. Em seguida, o programa deve
ler o valor da temperatura e então imprimir o valor correspondente à temperatura
na outra unidade de medida.
Observação: C = (5/9) * (F - 32) 
"""

temp = float(input("Digite a temperatura: "))
unit = input("Digite se a temperatura é em C ou F: ")

if (unit == 'F'):
    tempC = (5/9) * (temp - 32)
    print(f"\nA temperatura em Celsius = {tempC:.2f}")
elif (unit == 'C'):
    tempF = ((9/5) * temp) + 32
    print(f"\nA temperatura em Fahrenheit = {tempF:.2f}")
else:
    print("\nUnidade não encontrada. Tente novamente.")
