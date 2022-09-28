##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - Torre de Panquecas
# Nome: Enzo Emidio Ferreira
# RA: 243161
##################################################

# Leitura da torre de panquecas

torre = [int(panqueca) for panqueca in input().split()]

torreFinal = torre.copy()
torreFinal.sort()

# Leitura e processamento dos movimentos

pos = int(input())
while pos != 0:
    torreMov = torre[0:pos]
    torreMov.reverse()
    torre[0:pos] = torreMov
    pos = int(input())

# Impressão da saída

print("Torre estavel") if torreFinal == torre else print("Torre instavel")