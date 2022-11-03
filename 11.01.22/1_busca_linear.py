"""
Problema:
Dada uma sequência de valores e um valor alvo,
encontrar onde o alvo se localiza na sequência,
ou determinar que ele não ocorre

Entrada:
Uma sequência (lista, etc) e um alvo

Saída:
Índice do alvo na sequência, se houver,
ou -1/None, se não houver
"""

"""
Busca Linear
Algoritmo que percorre a sequência desde o início
coparando cada elemento com o alvo
Ao encontrar o valor alvo na sequência, para imediatamente
e informa o índice onde o alvo foi encontrado
"""

def buscaLinear(sequencia:list, alvo)->int:
    i = 0
    index = None
    encontrado = False
    while i <  len(sequencia) and encontrado == False:
        if sequencia[i] == alvo:
            encontrado = True
            index = i
        i += 1
    
    if index == None:
        return None
    else:
        return index
    
"""
Se a sequência tem n elementos,
demoramos n passos no pior caso

Custo: O(n)
"""
    
def main():
    nomes = ["Samuel", "Aldo", "Suzana", "Brunna", "Alberto"]
    
    i = buscaLinear(nomes, "Brunna") # i = nomes.index("Brunna")
    print(i) # 3
    
    j = buscaLinear(nomes, "Breno") # j = nomes.index("Breno") -> Gera ERRO!
    print(j) # None
main()