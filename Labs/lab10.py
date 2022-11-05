#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Caça ao Tesouro
# Nome: Enzo Emidio Ferreira
# RA: 243161
#####################################################

"""
Essa função recebe uma matriz e um nome (só para identificar)
E printa a matriz com cada elemento separado por espaços
e cada linha separada por uma quebra de linha
"""
def matrizShow(__matriz:list, __nome:str):
    print(f"Mostrando a matriz {__nome}...")
    for i in range(len(__matriz)):
        for j in range(len(__matriz[0])):
            print(f"\t{__matriz[i][j]}", end =" ")
        print()
    
"""
Essa função recebe uma matriz vazia e um inteiro N
Ela preenche a matriz até se tornar uma matriz None NxN
"""
def matrizNone(__matriz:list, n:int):
    for i in range(len(n)):
        linha = []
        for j in range(len(n)):
            linha.append(None)
        __matriz.append(linha)

# Dimensão da matriz mapa
n = int(input())

"""
Mapa em formato matricial nxn recebido por linha de input
separado por espaços onde:
"." -> Nada
"*" -> Tesouro
"""
mapa = [input().split() for _ in range(n)]

firstTeam = input()
scoreTeam1 = 0
scoreTeam2 = 0
qntPlayers = int(input())

"""
Matriz [i][j] que vai guardar os movimentos de cada jogador em uma linha
alternada entre os 2 times
i -> Par para o primeiro time e ímpar para o segunda
j -> Cada movimento:
    N: Cima (Norte)
    S: Baixo (Sul)
    O: Esquerda (Oeste)
    L: Direita (Leste)
"""
movimentos = []
for _ in range(qntPlayers):
    rawInput = input()
    linha = list(rawInput)
    movimentos.append(linha)
    
# matrizShow(movimentos, "movimentos")

for player in range(qntPlayers): # Loop para cada jogador
    # Cria o mapa do jogador preenchido de None
    mapaPercorrido = []
    matrizNone(mapaPercorrido, mapa)
    
    # Posições iniciais
    i = 0
    j = 0
    
    for jogada in range(len(movimentos[player])): # Loop para cada movimento
        # Identifica a direção do movimento
        if movimentos[player][jogada] == "N":
            i -= 1
        elif movimentos[player][jogada] == "S":
            i += 1
        elif movimentos[player][jogada] == "O":
            j -= 1
        elif movimentos[player][jogada] == "L":
            j += 1
        
        mapaPercorrido[i][j] = 1 # Preenche c/ 1 a posição do jogador
        if mapa[i][j] == "*": # Tesouro encontrado!
            # Pontuação para o time:
            if player % 2 == 0: # Time par
                scoreTeam1 += 1
            else: # Time ímpar
                scoreTeam2 += 1
            mapa[i][j] = "x" # Retira o tesouro do mapa
    
    # matrizShow(mapaPercorrido, f"Mapa percorrido do player {player + 1}")

scoreBlue, scoreRed = 0, 0
if firstTeam == "azul":
    scoreBlue, scoreRed = scoreTeam1, scoreTeam2
else:
    scoreBlue, scoreRed = scoreTeam2, scoreTeam1
    
# Impressão de saída

print(f"Tesouros encontrados pelo time azul: {scoreBlue}")
print(f"Tesouros encontrados pelo time vermelho: {scoreRed}")

if scoreBlue != scoreRed:
    print("Vitoria do time azul") if scoreBlue > scoreRed else print("Vitoria do time vermelho")
else: # Empate
    print("Empate")