"""
Exemplos de formas de escrever listas com list comprehension
"""

l = []

for i in range(3,10):
    l.append(i**3)

print(l)

# Equivalente a:

l = [i**3 for i in range(3,10)]
print(l)

# --------------------------------------

precosOriginais = [1000.0, 550.0, 635.0]
desconto = 0.3

precosDesconto = []
for preco in precosOriginais:
    precosDesconto.append(preco * (1 - desconto))
print(precosDesconto)

# Equivalente a:

precosOriginais = [1000.0, 550.0, 635.0]
desconto = 0.3

precosDesconto = [(1 - desconto) * preco for preco in precosOriginais]
print(precosDesconto)

# --------------------------------------

valores = [6, -1, 8, 0, -5, 6, 2, -2, -3]

valoresNegativos = []
for valor in valores:
    if valor < 0:
        valoresNegativos.append(valor)

print(valoresNegativos)

# Equivalente a:

valores = [6, -1, 8, 0, -5, 6, 2, -2, -3]

valoresNegativos = [n for n in valores if n < 0]
print(valoresNegativos)

# --------------------------------------

valores = [6, -1, 8, 0, -5, 6, 2, -2, -3]

sinais = ["Positivo" if n >= 0 else "Negativo" for n in valores]

print(valores)
print(sinais)

# --------------------------------------

precos = [1000.0, 550.0, 635.0]
descontos = [0.3, 0.15, 0.2]

precosFinais = []
for i in range(min(len(precos), len(descontos))):
    precosFinais.append(precos[i] * (1 - descontos[i]))
print(precosFinais)

# Equivale a:

precos = [1000.0, 550.0, 635.0]
descontos = [0.3, 0.15, 0.2]

precosFinais = [precos[i] * (1 - descontos[i]) for i in range(min(len(precos), len(descontos)))]
print(precosFinais)