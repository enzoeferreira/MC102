###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Controle de Estoque 2.0
# Nome: Enzo Emidio Ferreira
# RA: 243161
###################################################

# Leitura de dados
estoque = {}
produtos = [] # [[Nome, estoque, compras, vendas]]
              # [[0   ,       1,       2,      3]]
i = 0
rawEntrada = input()
while rawEntrada != "FIM":
    entrada = rawEntrada.split(" : ")
    
    if not entrada[0] in estoque:
    # Produto não cadastrado
        if int(entrada[1]) > 0:
        # Compra
            lista = [entrada[0], int(entrada[1]), 1, 0]
            produtos.append(lista)
            
            estoque[entrada[0]] = i # Guarda o indice da matriz produtos
            i += 1
        else:
        # Inválido
            print(f"Quantidade indisponivel para a venda de {int(entrada[1]) * (-1)} unidade(s) do produto {entrada[0]}.")
    else:
    # Produto cadastrado
        if int(entrada[1]) < 0:
        # Venda
            if produtos[estoque[entrada[0]]][1] >= int(entrada[1]) * (-1):
                # Venda possível
                produtos[estoque[entrada[0]]][1] += int(entrada[1]) # Atualiza estoque
                produtos[estoque[entrada[0]]][3] += 1 # Contabiliza venda
            else:
                # Venda impossível
                print(f"Quantidade indisponivel para a venda de {int(entrada[1]) * (-1)} unidade(s) do produto {entrada[0]}.")
        if int(entrada[1]) > 0:
        # Compra
            produtos[estoque[entrada[0]]][1] += int(entrada[1]) # Atualiza estoque
            produtos[estoque[entrada[0]]][2] += 1 # Contabiliza compra
        
    rawEntrada = input()
# Impressão da saída
produtos.sort()
for i in range(len(produtos)):
    print("Produto:", produtos[i][0])
    print("Quantidade em Estoque:", produtos[i][1])
    print("Pedidos de Compra:", produtos[i][2])
    print("Pedidos de Venda:", produtos[i][3])