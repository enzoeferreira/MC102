"""
Essa função recebe duas matrizes
e retorna sua soma
"""
def soma_matrizes(M1, M2):
    M = [] # Resultado
    for i in range(len(M1)):
        M.append(M1[i].copy)
        for j in range(len(M1[0])):
            M[i][j] += M2 [i][j]
            
    return M