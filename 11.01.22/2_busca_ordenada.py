"""
Busca em Sequência Ordenada:
Igual ao problema geral da busca
porém restrito a sequências ordenadas
"""

def buscaOrdenada(sequencia:list, alvo)->int: # Sequência em ordem crescente!
    i = 0
    index = None
    encontrado = False
    while i <  len(sequencia) and encontrado == False and sequencia[i] <= alvo:
        if sequencia[i] == alvo:
            encontrado = True
            index = i
        i += 1
    
    if index == None:
        return None
    else:
        return index
    
"""
Para de buscar se me deparar com
um valor maior que o alvo,
pois a sequência está em ordem crescente

Se a sequência tem n elementos,
demoramos n passos no pior caso
    
Portanto essa versão será mais rápida que a busca linear
em alguns casos, mas sua análise de pior caso ainda é a mesma.

Custo: O(n)
"""

def main():
    numeros = [1, 2, 3, 6, 7, 11, 16]
    
    i = buscaOrdenada(numeros, 7)
    print(i) # 4
main()