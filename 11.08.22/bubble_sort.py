"""
Essa função realiza uma passada
do algoritmo de ordenação Bubble Sort
do início ao fim da lista
"""
def oneRun(__lista:list):
    for i in range(len(__lista) - 1):
        if __lista[i] > __lista[i + 1]:
            __lista[i], __lista[i + 1] = __lista[i + 1], __lista[i]
            
"""
Versão 0 do Bubble Sort

Faz n-1 passadas (completas) na lista
"""
def bubbleSort0(__lista:list):
    for _ in range((len(__lista)) - 1):
        oneRun(__lista)
        
        print(__lista)
        input()
        
"""
Realiza uma passada do Bubble Sort
indo do índice 0 até um índice limite
que é fornecido como parâmetro

Devolve TRUE, se realizar alguma troca
        FALSE, caso contrário
"""
def runUntilIndex(__lista:list, __limite:int):
    trocou = False
    for i in range(__limite):
        if __lista[i] > __lista[i + 1]:
            __lista[i], __lista[i + 1] = __lista[i + 1], __lista[i]
            trocou = True
    
    return trocou
            

"""
Versão 1 do Bubble Sort

Faz n-1 passadas na lista
porém cada passada é mais curta que a anterior
"""
def bubbleSort1(__lista:list):
    k = 1
    for _ in range(len(__lista) - 1):
        runUntilIndex(__lista, len(__lista) - k)
        
        print(f"Passada foi até o índice {len(__lista) - k}")
        print(__lista)
        input()
        
        k += 1
        
"""
Versão FINAL do Bubble Sort:

A cada passada, verifica se são feitas trocas
Se não for feita nenhuma troca, não precisa
continuar a execução do algoritmo
"""
def bubbleSortFinal(__lista:list):
    k = 1
    for _ in range(len(__lista) - 1):
        fezTroca = runUntilIndex(__lista, len(__lista) - k)
        
        print(f"Passada foi até o índice {len(__lista) - k}")
        print(__lista)
        input()
        
        # Se não realizei nenhuma troca, a lista já está ordenada
        if not fezTroca:
            print("Nenhuma troca foi realizada! Lista ordenada.")
            break
        
        
        k += 1

def mainTest():
    lista = [1, 2, 3, 4, 6, 5]
    print("Bubble Sort versão 0:")
    bubbleSort0(lista)
    
    print("Bubble Sort versão 1:")
    bubbleSort1(lista)
    
    print("Bubble Sort final:")
    bubbleSortFinal(lista)
# mainTest()

def bubbleSort(__lista:list):
    k = 1
    fezTroca = True
    
    while k <= len(__lista) - 1 and fezTroca:
        fezTroca = runUntilIndex(__lista, len(__lista) - k)
        k += 1