"""
Transformar uma sequência de inteiros dada por
uma única linha de input em uma lista de inteiros

Ex:
input: 10 20 30 40 50
output: [10, 20, 30, 40, 50]
"""

rawInput = input().split()
valores = [int(valor) for valor in rawInput]

# Equivalente a:

valores = list(map(int, input().split()))

# Equivalente a:

valores = [int(valor) for valor in input().split()]