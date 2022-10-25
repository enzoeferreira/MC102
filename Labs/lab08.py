###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Wordle
# Nome: Enzo Emidio Ferreira
# RA: 243161
###################################################

# Leitura da palavra
palavra = input()
palavraList = list(palavra)

# Leitura dos palpites e impressão do resultado para cada palpite

vencedor = False
tentativas = 0
while tentativas < 6 and vencedor == False:
    palpiteIn = input()
    palpiteList = list(palpiteIn)
    
    for i in range(len(palavraList)):
        if palpiteList[i] in palavraList:
            if palpiteList[i] == palavraList[i]:
                # Letra está na palavra e na posição correta
                palpiteList[i] = palpiteList[i].upper()
            # Se não: Letra está na palavra mas na posição errada
        else:
            palpiteList[i] = "_"
    print("".join(palpiteList))
    
    if "".join(palpiteList).lower() == palavra:
        vencedor = True
    
    tentativas += 1

# Impressão da linha final
if vencedor == True:
    print("Resposta correta")
else:
    print("Palavra correta:", palavra)