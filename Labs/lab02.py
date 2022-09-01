###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Rumo a Marte
# Nome: Enzo Emidio Ferreira
# RA: 243161
###################################################

# Leitura de dados

D1 = int(input())
V1 = int(input())
T = int(input())
D2 = int(input())
V2 = int(input())

# Cálculo do tempo total gasto por cada espaçonave 

tempoSpaceX = (D1 / V1) / 24
tempoBlueOrigin = (D2 / V2) / 24

# Impressão da resposta

if T + tempoBlueOrigin > tempoSpaceX:
    print(True)
else:
    print(False)
