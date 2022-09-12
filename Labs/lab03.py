###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Ingresso do Cinema
# Nome: Enzo Emidio Ferreira
# RA: 243161
###################################################

# leitura de dados

diaDaSemana = int(input())
horaSessao = int(input())
minutoSessao = int(input())
estudante = input()
pagamento = input()

# dados

if pagamento == 'C':
    desconto = True
else:
    desconto = False
    
precoTarde = [30, 15, 15, 15, 20, 20, 30]
precoNoite = [30, 20, 20, 30, 30, 40, 40]
promocaoTarde = [0.7, 0.5, 0.5, 0.5, 0.5, 0.5, 0.8]
promocaoNoite = [0.7, 0.5, 0.5, 0.5, 0.5, 0.7, 0.8]

# valor a pagar

if (horaSessao < 18) or (horaSessao == 18 and minutoSessao < 30):
    ingresso = precoTarde[diaDaSemana - 1]
    if estudante == 'S':
        ingresso = ingresso * 0.5
    else:
        if desconto == True:
            ingresso = ingresso * promocaoTarde[diaDaSemana - 1]
else:
    ingresso = precoNoite[diaDaSemana - 1]
    if estudante == 'S':
        ingresso = ingresso * 0.5
    else:
        if desconto == True:
            ingresso = ingresso * promocaoNoite[diaDaSemana - 1]

# saída do valor do ingresso
print('Valor do ingresso: R$', format(ingresso, '.2f').replace('.', ','))