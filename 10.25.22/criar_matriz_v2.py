"""
Cria uma matriz recebendo cada linha separando elementos por espaço
"""

l = int(input("Quantas linhas? "))

matriz = []

for i in range(l):
    linha = [int(valor) for valor in input().split()]
    matriz.append(linha)
    
print("Sua matriz é:")
for i in range(l):
    for j in range(len(matriz[0])):
        print(matriz[i][j], end=" ")
    print()