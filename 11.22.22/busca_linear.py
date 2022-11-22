"""Tarefas recursivas envolvendo sequências
Exercício: Escrever uma função recursiva
que recebe uma lista e um alvo e devolve:
-> True: Se o alvo existe na lista
-> False: Caso contrário
"""

def buscaV1(valores:list, alvo)->bool:
    if valores == []:
        # Caso Base
        return False
    if valores[0] == alvo:
        return True
    return buscaV1(valores[1:], alvo)

# Refatorando
def buscaV2(valores:list, alvo)->bool:
    if valores == []:
        return False
    if valores[0] == alvo or buscaV2(valores[1:], alvo):
        # Se a 1a condição for TRUE, retorna TRUE e não executa a recursão
        return True
    return False

# Como temos uma expressão redundante do tipo:
#     if <condição>:
#         return True
#     else:
#         return False
# Substituimos por
#     return <condição>
 
def buscaV3(valores:list, alvo)->bool:
    if valores == []:
        return False
    return valores[0] == alvo or buscaV3(valores[1:], alvo)

# Sem usar o slice para otimizar uso de memória
def busca(valores:list, alvo, inicio = 0)->bool:
    if inicio == len(valores):
        # Percorreu a lista toda
        return False
    return valores[inicio] == alvo or busca(valores, alvo, inicio + 1)

import email