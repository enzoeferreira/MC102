"""
Cria uma matriz recebendo elemento por elemento
"""

m = int(input("Quantas linhas? "))
n = int(input("Quantas colunas? "))

matriz = []
for i in range(m):
    linha = []
    for j in range(n):
        x = int(input(f"[{i}][{j}] = "))
        linha.append(x)
    matriz.append(linha)

for i in range(m):
    for j in range(n):
        print(matriz[i][j], end = " ")
    print()