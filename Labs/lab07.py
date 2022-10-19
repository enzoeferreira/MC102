###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Disconnect
# Nome: Enzo Emidio Ferreira
# RA: 243161
###################################################

# Leitura das tropas de defesa

tropasDef = []
tropas = int(input())

for i in range(tropas):
    tropa = int(input())
    tropasDef.append(tropa)

# Leitura das tropas de ataque

tropasAtk = []
tropas = int(input())

for i in range(tropas):
    tropa = int(input())
    tropasAtk.append(tropa)

# Processamento da guerra
            
# print(tropasDef)
# print(tropasAtk)
j = 0
vencedores = False

while vencedores == False and j <= len(tropasDef) - len(tropasAtk):
    derrota = 0
    empate = 0
    vitoria = 0
    # print(f"------ Batalha {j + 1} ------")
    # print("i =", i)
    # print("j =", j)
    for i in range(len(tropasAtk)):
        # print(f"Defensor {tropasDef[j + i]} vs Atacante {tropasAtk[i]}")
        if tropasDef[j + i] > tropasAtk[i]:
            derrota += 1
            # print("Perdemos...")
        elif tropasDef[j + i] == tropasAtk[i]:
            empate += 1
            # print("Empatamos.")
        else:
            vitoria += 1
            # print("Vencemos!")
            
    # print("No total obtivemos:")
    # print("Derrotas =", derrota)
    # print("Empates =", empate)
    # print("Vitorias =", vitoria)
    if derrota >= vitoria:
        j += 1
        # print("Perdemos a guerra...")
    else:
        vencedores = True
        # print("Vencemos a guerra!")    

# Saída de dados

# print("-----------------------------")
print("Derrota") if vencedores == False else print('Vitória posicionando as tropas a partir da posição', j + 1)