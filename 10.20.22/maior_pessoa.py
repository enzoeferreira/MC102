"""
Essa função recebe um dicionário
e retorna o maior valor contido nesse dicionário
e a chave a que este valor esta associado
"""

def maximo_e_chave(dicionario: dict):
    chaves = list(dicionario.keys())
    valorMax = dicionario[chaves[0]]
    chaveMax = chaves[0]
    
    for chave in chaves:
        if dicionario[chave] > valorMax:
            valorMax = dicionario[chave]
            chaveMax = chave
            
    return chaveMax, valorMax
            
altura = {
    "Agnaldo": 1.78,
    "Bernardo": 1.65,
    "Carlos": 1.84,
    "Denis": 1.55
}

maiorPessoa, maiorAltura = maximo_e_chave(altura)

print(f"A pessoa mais alta é {maiorPessoa} com {maiorAltura}m de altura.")