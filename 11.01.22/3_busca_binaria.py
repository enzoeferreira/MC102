"""
Busca Binária
Vamos sucessivas vezes dividir a sequência entre
uma região com elementos "pequenos" e uma outra
região com elementos "grandes"
É chamada de binária pois faz classificação binária
entre pequenos e grandes
"""

def buscaBinaria(sequencia:list, alvo): # Sequência ORDENADA
    # Índices ini e fim delimitam a região viável para busca
    ini = 0
    fim = len(sequencia) - 1
    
    while fim - ini >= 0: # Quando ini == fim, temos ainda um elemento
        meio = (ini + fim) // 2
        if sequencia[meio] == alvo:
            return meio # Encontrei o alvo!
        elif sequencia[meio] > alvo:
            fim = meio - 1 # Do meio para frente todos são maiores
        elif sequencia[meio] < alvo:
            ini = meio + 1 # Do meio para tras todos são menores
    return None

def main():
    # Exemplo 1
    lista1 = [1, 2, 3, 6, 7, 11, 16]
    
    index7 = buscaBinaria(lista1, 7)
    index8 = buscaBinaria(lista1, 8)
    print(f"Elemento 7 está na posição {index7}")
    print(f"Elemento 8 está na posição {index8}")
    
    # Exemplo 2
    lista2 = [4, 11, 18, 26, 50, 63, 77, 91]
    
    index18 = buscaBinaria(lista2, 18)
    print(f"Elemento 18 está na na posição {index18}")
main()