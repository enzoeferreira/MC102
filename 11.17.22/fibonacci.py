"""
A função abaixo recebe um inteiro n >= 0 e
devolve o valor de fn, isto é, o n-ésimo número
na sequência de Fibonacci
"""

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)