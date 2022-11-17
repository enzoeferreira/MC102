#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Encaixe 2D
# Nome: Enzo Emidio Ferreira
# RA: 243161
#####################################################

"""
Essa função printa a matriz recebida como argumento
separando seus elementos por um espaço
"""

def mostrarMatriz(matriz:list):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(f"{matriz[i][j]} ", end = "")
        print()
    
"""Testa se a peça encaixa no tabuleiro

Teste se a peça, em determinada posição inicial (Canto Superior Esquerdo),
se encaixa no tabuleiro.

Args:
    tabuleiro: Matriz do tabuleiro
    peca: Matriz da peça que irá se encaixar no tabuleiro
    iIncial: Inteiro que representa a linha inicial
    jInicial: Inteiro que representa a coluna inicial

Returns:
    Um booleano:
    True: Peça se encaixa
    False: Peça não se encaixa
"""
def testeEncaixe(tabuleiro:list, peca:list,
                 iInicial:int, jInicial:int)->bool:
    falhou = False
    for i in range(len(peca)):
        if falhou == True:
            break
        else:
            for j in range(len(peca[0])):
                # print(f"-> Peça {i},{j} em {i + iInicial},{j + jInicial}")
                if (peca[i][j] == "X" and
                    tabuleiro[i + iInicial][j + jInicial] == "X"):
                    # Peça tentando encaixar fora do buraco
                    falhou = True
                    break
                
    if falhou == False:
        return True
    else:
        return False

"""Rotaciona a matriz

Rotaciona a matriz em 90° (Sentido Horário)

Args:
    peca: Matriz a ser rotacionada

Returns:
    A matriz rotacionada em 90° sentido horário
"""
def rotacionarMatriz(peca:list):
    pecaRotacionada = []
    for j in range(len(peca[0])):
        linhaRotacionada = []
        for i in range(len(peca) - 1, -1, -1):
            linhaRotacionada.append(peca[i][j])
        pecaRotacionada.append(linhaRotacionada)
    
    return pecaRotacionada

# Leitura do tabuleiro
T = int(input())
tabuleiro = []
for _ in range(T):
  tabuleiro.append(input().split())

# Leitura da peça
P = int(input())
peca = []
for _ in range(P):
  peca.append(input().split())

encaixes = [0, 0, 0, 0] # Quant. de encaixes possíveis em cada rotação
                        # [Original, 90°, 180°, 270°]

posMax = (len(tabuleiro) - len(peca), len(tabuleiro[0]) - len(peca[0]))
linhaMax, colunaMax = posMax
for modo in range(4): # Testa os encaixes para cada rotação da matriz
    for linha in range(linhaMax + 1):
        for coluna in range(colunaMax + 1):
            # print(f"Analisando peça modo {modo} em {linha},{coluna}")
            if testeEncaixe(tabuleiro, peca, linha, coluna) == True:
                # Encaixe bem sucedido
                encaixes[modo] += 1
                
    peca = rotacionarMatriz(peca) # Rotaciona a peça
    
    # Atualiza a posição máxima de análise com a peça rotacionada
    posMax = (len(tabuleiro) - len(peca), len(tabuleiro[0]) - len(peca[0]))
    linhaMax, colunaMax = posMax
            
# Impressão de Saída
encaixes = list(map(str, encaixes)) # Casting de str na lista encaixes
print(",".join(encaixes)) # Printa o resultado em formato "x,y,z,w"