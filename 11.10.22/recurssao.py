def fatorial(n:int) -> int:
    if n == 0:
        return 1
    
    return n * fatorial(n - 1)

def potencia(base, expoente:int):
    if expoente == 0:
        return 1
    
    return base * potencia(base, expoente - 1)