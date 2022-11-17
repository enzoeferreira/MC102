def sucessor(n):
    if n % 2 == 0:
        return n // 2
    return (3 * n) + 1

def mostraSequencia(n):
    if n == 1:
        print(1)
    else:
        print(n)
        mostraSequencia(sucessor(n))

"""
Refatoração da função anterior
"""
def mostraSequencia(n):
    print(n)
    if n > 1:
        mostraSequencia(sucessor(n))
        
def comprimento(n):
    if n == 1:
        return 0
    return 1 + comprimento(sucessor(n))

def main():
    i = 1
    maiorComprimento = comprimento(i)
    maiorNumero = i
    while True:
        i += 1
        if comprimento(i) > maiorComprimento:
            maiorComprimento = comprimento(i)
            maiorNumero = i
        print(f"Maior: {maiorNumero}, {maiorComprimento} passos")
main()