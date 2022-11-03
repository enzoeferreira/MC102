"""
Essa função recebe uma lista e ordenada essa lista
através do algoritmo de busca "Selection Sort"
"""
def selectionSort(lista:list):
    for i in range(len(lista) - 1):
        # Vamos buscar o menor elemento em lista[i:] e coloca na posição i
        indiceMin = selectMin(lista, i)
        lista[i], lista[indiceMin] = lista[indiceMin], lista[i]

"""
Essa função recebe uma lista e um índice de início
e retorna o índice do menor elemento
encontrado do início em diante
"""
def selectMin(lista:list, inicio:int):
    min = lista[inicio]
    indice = inicio
    for i in range(inicio + 1, len(lista)):
        if lista[i] < min:
            min = lista[i]
            indice = i
            
    return i

def main():
    a = 1
main()