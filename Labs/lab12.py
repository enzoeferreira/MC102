###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - Redimensionamento de Imagens
# Nome: Enzo Emidio Ferreira
# RA: 243161
###################################################

def imprimir_imagem(imagem):
    print("P2")
    print(len(imagem[0]), len(imagem))
    print("255")
    for i in range(len(imagem)):
        print(" ".join(str(int(x)) for x in imagem[i]))

def matrizNoneExpansao(matriz:list):
    matrizNone = []
    for i in range((len(matriz) * 2) - 1):
        linha = []
        for j in range((len(matriz[0]) * 2) - 1):
            linha.append(None)
        matrizNone.append(linha)
        
    return matrizNone

def matrizNoneRetracao(matriz:list):
    matrizNone = []
    m = len(matriz)
    n = len(matriz[0])
    
    if m % 2 == 0:
        rangeM = m // 2
    else:
        rangeM = (m + 1) // 2
    if n % 2 == 0:
        rangeN = n // 2
    else:
        rangeN = (n + 1) // 2
        
    for i in range(rangeM):
        linha = []
        for j in range(rangeN):
            linha.append(None)
        matrizNone.append(linha)
        
    return matrizNone

def expansao(imagem_original):
    imagem = matrizNoneExpansao(imagem_original)

    for iA in range(1, len(imagem_original) + 1):   
        iB = (iA * 2) - 1
        for jA in range(1, len(imagem_original[0]) + 1):
            jB = (jA * 2) - 1
            imagem[iB - 1][jB - 1] = imagem_original[iA - 1][jA - 1]
    
    for iB in range(len(imagem)):
        for jB in range(len(imagem[0])):
            if (iB + 1) % 2 != 0 and (jB + 1) % 2 == 0: # iB ímpar e jB par
                mediaH = (imagem[iB][jB-1] + imagem[iB][jB+1]) // 2
                imagem[iB][jB] = mediaH
            elif (iB + 1) % 2 == 0 and (jB + 1) % 2 != 0: # iB par e jB ímpar
                mediaV = (imagem[iB-1][jB] + imagem[iB+1][jB]) // 2
                imagem[iB][jB] = mediaV
                
    for iB in range(len(imagem)):
        for jB in range(len(imagem[0])):
            if (iB + 1) % 2 == 0 and (jB + 1) % 2 == 0: # iB par e jB par
                mediaH = (imagem[iB][jB-1] + imagem[iB][jB+1]) // 2
                mediaV = (imagem[iB-1][jB] + imagem[iB+1][jB]) // 2
                
                media = (mediaH + mediaV) // 2
                imagem[iB][jB] = media
                      
    return imagem

def retracao(imagem_original):
    imagem = matrizNoneRetracao(imagem_original)
    for i in range(len(imagem)):
        for j in range(len(imagem[0])):
            if (len(imagem_original[0]) % 2 != 0 and
                j*2 + 1 == len(imagem_original[0]) and
                i*2 + 1 != len(imagem_original)):
                # Colunas totais ímpares e
                # Última coluna da imagem original
                # Não é a última linha da imagem original
                # Matriz 2x1
                imagem[i][j] = (imagem_original[i*2][j*2] +
                                imagem_original[i*2 + 1][j*2]) // 2
            elif (len(imagem_original) % 2 != 0 and
                i*2 + 1 == len(imagem_original) and
                j*2 + 1 != len(imagem_original[0])):
                # Linhas totais impares e
                # Última linha da imagem original e
                # Não é a última coluna da imagem original
                # Matriz 1x2
                imagem[i][j] = (imagem_original[i*2][j*2] +
                                imagem_original[i*2][j*2 + 1]) // 2
            elif (len(imagem_original) % 2 != 0 and
                i*2 + 1 == len(imagem_original) and
                j*2 + 1 == len(imagem_original[0])):
                # Linhas e colunas totais impares
                # Última linha e coluna da imagem original
                # Mesmo elemento
                imagem[i][j] = imagem_original[i*2][j*2]
            else:
                imagem[i][j] = (imagem_original[i*2][j*2] +
                            imagem_original[i*2][j*2 + 1] +
                            imagem_original[i*2 + 1][j*2] +
                            imagem_original[i*2 + 1][j*2 + 1]) // 4
            
    return imagem

# leitura da imagem
input() # P2 - linha a ser ignorada

m, n = [int(x) for x in input().split()]

input() # 255 - linha a ser ignorada

imagem_original = []
for i in range(n):
    linha = [int(x) for x in input().split()]
    imagem_original.append(linha)

# leitura do tipo de redimensionamento

redimensionamento = input()
if redimensionamento == "expansao":
    imagem = expansao(imagem_original)
elif redimensionamento == "retracao":
    imagem = retracao(imagem_original)

# impressão da imagem final
imprimir_imagem(imagem)