"""
Ler da entrada uma lista de nomes.
O fim da entrada é marcado pela entrada de uma string vazia
(Ou seja, a pessoa da <ENTER> sem escrever nada)

a) Ao final, imprimir os nomes em ordem alfabética
b) Imprimir apenas nomes únicos (não imprimir repetidos)
"""

nomes = []

entrada = input()
nomes.append(entrada)
while entrada != "":
    entrada = input()
    if not entrada in nomes and entrada != "":
        nomes.append(entrada)
        
nomes.sort()

print(nomes)