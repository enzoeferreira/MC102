"""
Esta função que recebe dois valores
e retorna a soma entre eles
"""

def soma(a, b):
    return a + b

n = soma(2, 9)
print(f"Soma de 2 com 9 = {n}")

l = soma([1, 2], [3, 4, 5])
print(f"Soma de [1, 2] com [3, 4, 5] = {l}") # Soma de 2 listas

"""
Esta função que recebe uma lista de valores
e retorna o produto entre eles
"""

def produto(valores:list):
    resultado = 1
    for valor in valores:
        resultado = resultado * valor       
    return resultado

n = produto([4, 3, 6])
print(f"Produto entre 4, 3 e 6 = {n}")

"""
Esta função que recebe um valor inteiro n
e retorna seus divisores de 1 a n
"""

def divisores(n:int)->list:
    div = []
    for i in range(1, n):
        if n % i == 0:
            div.append(i)
    return div

n = divisores(6)
print(f"Divisores de 6 são: {n}")

"""
Esta função que recebe um nome e mostra na tela
uma mensagem de despedida para esse nome

OBS: Retorna NONE
"""

def despede(nome):
    print(f"Tchau, {nome}!")
    
x = despede("Agnaldo")
print(x) # Irá printar NONE