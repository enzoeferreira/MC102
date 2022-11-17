def mostraListaV1(lista:list):
    if lista == []:
        print()
    else:
        print(lista[0])
        resto = lista[1:]
        mostraListaV1(resto)
        
def mostraListaV2(lista:list):
    if lista != []:
        print(lista[0])
        resto = lista[1:]
        mostraListaV2(resto)
    
def mostraLista(lista:list, inicio:int = 0):
    if inicio < len(lista):
        print(lista[inicio])
        mostraLista(lista, inicio + 1)