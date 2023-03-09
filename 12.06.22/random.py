"""
Em programação geralmente a seed é o horário atual em segundos
"""

import random

random.randint(a, b) # Retorna um número aleatório de "a" a "b"
random.seed() # Seta uma seed
random.random() # Float entre 0 e 1 

def umPonto():
    x, y = random.random(), random.random()
    dist_origem = (x**2 + y**2)** 0.5
    return (dist_origem <= 1)

def estimaPi(N = 1e6):
    N = int(N)
    dentro = 0 # Quantos pontos caem dentro do circulo unitário
    
    for _ in range(N):
        if umPonto():
            dentro += 1
    return (dentro / N) * 4 # Aproximação de pi