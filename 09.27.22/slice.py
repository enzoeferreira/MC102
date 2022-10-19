"""
Exemplos de uso do slice em listas
"""

valores = [2, 3, 5, 7, 11, 13, 17, 19, 23]

primeirosTres = [valores[i] for i in range(3)]
posicoesPares = [valores[i] for i in range(0, len(valores), 2)]
print(primeirosTres)
print(posicoesPares)

# Equivale a:

primeirosTres = valores[:3]
posicoesPares = valores[0::2]
print(primeirosTres)
print(posicoesPares)

# --------------------------------------

tempMensal = [11.2, 18.5, 21.1, 20.7, 22.5, 24.8, 26.6, 25.1, 21.0, 17.1, 16.5, 13.5]

abrilAJulho = tempMensal[3:7]       # [20.7, 22.5, 24.8, 26.6]
ultimoTrimestre = tempMensal[9:]    # [17.1, 16.5, 13.5]
primeiroSemestre = tempMensal[:6]   # [11.2, 18.5, 21.1, 20.7, 22.5, 24.8]
contrario = tempMensal[::-1]        # Lista invertida