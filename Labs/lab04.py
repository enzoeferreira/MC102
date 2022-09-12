###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Controle de Estoque
# Nome: Enzo Emidio Ferreira
# RA: 243161
###################################################

# leitura da sequência de compras e vendas

vendas = 0
indisponiveis = list()
estoque = 0

entrada = int(input())

if entrada < 0:
    indisponiveis.append(entrada)
else:
    estoque = entrada

while entrada != 0:
    entrada = int(input())
    
    if entrada < 0:
        if estoque + entrada >= 0:
            vendas += 1
            estoque += entrada
        else:
            indisponiveis.append(entrada)
    else:
        estoque += entrada

# impressão da saída

for indisponivel in indisponiveis:
    print(f"Quantidade indisponível para a venda de {indisponivel * -1} unidades.")

print(f"Quantidade de vendas realizadas: {vendas}")
print(f"Quantidade em estoque: {estoque}")