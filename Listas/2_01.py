"""
Considere o seguinte menu:
1 - Pizza Marguerita
2 - Pizza de Calabresa
3 - Pizza de Pepperoni
4 - Pizza de Mussarela
5 - Sair
O seu programa deve: imprimir o menu; ler um número de 1 até 5; e imprimir a opção do
menu correspondente ao número lido. Isso deve ser repetido até que o usuário selecione a
opção 5.
"""

menu = ["Marguerita", "de Calabresa", "de Pepperoni", "de Mussarela"]
item = 0

while item != 5:
    item = int(input("Qual item do menu? "))
    if item != 5:
        print(f"Pizza {menu[item - 1]}")