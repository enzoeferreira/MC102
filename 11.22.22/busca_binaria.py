"""Tarefas recursivas envolvendo sequências

Exercício: Algoritmo de busca binária
implementado por função recursiva
"""

def buscaBinaria(valores:list, alvo, inicio:int, fim:int)->bool:
    if inicio > fim:
        # Região viável vazia
        return False
    meio = (inicio + fim) // 2
    if valores[meio] == alvo:
        # Alvo encontrado
        return True
    if valores[meio] > alvo:
        return buscaBinaria(valores, alvo, inicio, meio - 1)
    return buscaBinaria(valores, alvo, meio + 1, fim)


"""Função "Wrapper" para busca binária

Não posso fazer direto fim = len(valores) - 1 pois o interpretador
precisa saber qual o valor padrão antes do programa ser executado,
por isso essa função é importante para facilitar o uso do "cliente"
"""

def busca(valores:list, alvo):
    return buscaBinaria(valores, alvo, 0, len(valores) - 1)

# Outra possibilidade para inicializar fim como len(valores) - 1 por padrão:
# OBS: Não muito elegante!
def _buscaBin(valores:list, alvo, inicio = 0, fim:int = None)->bool:
    if fim == None:
        fim = len(valores) - 1
    # ...
    
"""Retorna o índice do alvo

Busca binária igual a função superior mas ao invés de retornar um bool
retorna o índice do elemento caso encontrado, caso contrário retorna None
"""

def buscaBinariaIndice(valores:list, alvo, inicio:int, fim:int)->bool:
    if inicio > fim:
        # Região viável vazia
        return None
    meio = (inicio + fim) // 2
    if valores[meio] == alvo:
        # Alvo encontrado
        return meio
    if valores[meio] > alvo:
        return buscaBinaria(valores, alvo, inicio, meio - 1)
    return buscaBinaria(valores, alvo, meio + 1, fim)