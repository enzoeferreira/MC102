m = [[9, 6, 5],
     [1, 4, 2],
     [8, 0, 7],
     [-3, 2, 0]]

print(len(m))       # 4
print(m[1])         # [1, 4, 2]
print(len(m[1]))    # 3
print(m[2][0])      # 8 // (m[2] = [8, 0, 7], o indíce 0 é 8)

"""
Esta é uma convenção de uso de matrizes
muito comum na computação:

INDEXAÇÃO POR LINHA

-> É fácil acessar uma linha específica
-> Obter uma coluna exige um laço de repetição

Está função recebe uma matriz
e retorna seu n° de linhas e colunas,
nesta ordem
"""

def dimensões(m:list): # Versão 0
    linhas = len(m)
    colunas = len(m[0]) # Estou confiando que toda linha tem o mesmo len
    return linhas, colunas

"""
Continuando o código...
"""

l, c = dimensões(m)
print(f"{l} linhas, {c} colunas") # 4 linhas, 3 colunas
print(f"Ou seja, {l*c} elementos no total.")

"""
A função abaixo recebe uma matriz m e um índice i
e retorna uma cópia da linha m[i]
"""

def copiaLinha(m:list, i:int):
    linha = []
    for valor in m[i]:
        linha.append(valor)
        
    return linha
    # ou apenas: return m[i].copy()

x = copiaLinha(m, 1)
print("Função copiaLinha:", x) # [1, 4, 2]

"""
A função abaixo recebe uma matriz m e um índice j
e retorna uma lista contendo a coluna j de m
"""

def copiaColuna(m:list, j:int):
    coluna = []
    for linha in m:
        coluna.append(linha[j])
        
    return coluna

y = copiaColuna(m, 2)
print("Função copiaColuna:", y) # [5, 2, 7, 0]

"""
Esta função recebe uma matriz
e printa a matriz
"""

def mostraMatriz(m:list):
    l, c = dimensões(m)
    for i in range(l):
        for j in range(c):
            print(f"\t{m[i][j]}", end=" ") # \t corrige desalinhamento c/ tab
        print()
        
print("Matriz m:")
mostraMatriz(m)

"""
Esta função recebe uma matriz m
e retorna uma cópia dela com todos elementos
multiplicados por 3
"""

def triplicaMatriz(m:list):
    nova = []
    for linha in m:
        nova.append([3*x for x in linha])
    
    return nova

m3 = triplicaMatriz(m)
print("Matriz m*3:")
mostraMatriz(m3)

"""
Produto interno (dot product) é, por exemplo:
[6, 4, 10] * [3, 7, 2] = 6*3 + 4*7 + 10*2 = 66

Esta função recebe 2 listas x e y
e retorna o resultado do produto interno entre elas
"""

def produtoInterno (x:list, y:list):
    if len(x) != len(y):
        print("ERRO: Vetores de diferentes dimensões!")
        return None
    
    result = 0
    for i in range(len(x)):
        result += x[i] * y[i]
        
    return result

    # Ou: return sum([x[i] * y[i] for i in range(len(x))])

"""
Esta função recebe uma matriz A e B
e retorna uma matriz C resultante do produto matricial delas
"""

def produtoMatricial(A:list, B:list):
    linhasA, colunasA = dimensões(A)
    linhasB, colunasB = dimensões(B)
    if colunasA != linhasB:
        print("ERRO: Matrizes incompatíveis para produto matricial.")
        return None

    # Cria matriz com dimensçoes adequadas preenchida com None
    C = [[None for j in range(colunasB)] for i in range(linhasA)]
    
    for i in range(linhasA):
        for j in range(colunasB):
            C[i][j] = produtoInterno(A[i], copiaColuna(B, j))
# ou:
# C = [[produtoInterno(A[i], copiaColuna(B, j)) for j in range(colunasB)] for i in range(linhasA)]
            
    return C

A = [[1, 2, 3],
     [3, 0, 1]]
B = [[2, 4],
     [1, 6],
     [2, 0]]
    
print("Produto da matriz A com B:")
mostraMatriz(produtoMatricial(A, B))