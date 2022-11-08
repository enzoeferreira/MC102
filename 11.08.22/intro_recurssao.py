def fatorial(n):
    if n == 0:  # Base
        return 1
    else:       # Caso Geral
        return fatorial(n-1)*n
    
def mainFatorial():
    print(fatorial(5))
    print(fatorial(3))
mainFatorial()

def exemplo(n):
    if n > 0:
        print("Oi", n)
        input()
        exemplo(n - 1)
        
def mainExemplo():
    exemplo(3)
mainExemplo()