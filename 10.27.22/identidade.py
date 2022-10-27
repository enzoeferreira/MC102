"""
EXERCÍCIO
Escrever uma função que cumpra a especificação:
A função abaixo recebe um inteiro (positivo) n e
devolve a matriz In (Identidade nxn).
"""

def identidade(n:int)->list:
    matriz = []
    for i in range(n):
        linha = [1 if i == j else 0 for j in range(n)]
        matriz.append(linha)
    
    # ou: return [[0 if i != j else 1 for j in range(n)] for i in range(n)]
    return matriz

def main():
    n = int(input("Digite um inteiro n positivo: "))
    matriz = identidade(n)
    for i in range(n):
        for j in range(n):
            print(f"\t{matriz[i][j]}", end=" ")
        print()
main()