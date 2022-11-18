###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Eleições 2022
# Nome: Enzo Emidio Ferreira
# RA: 243161
###################################################

# Leitura de dados

urna = {}
while True:
    entrada = input()
    if entrada == "0":
        # Finaliza contagem de votos
        break

    if entrada not in urna.keys():
        # Cadastra candidato com 1 voto
        urna[entrada] = 1
    else:
        # Candidato já cadastrado, contabiliza voto
        urna[entrada] += 1
        
candidatos = []
for key in urna.keys():
    tupla = (urna[key], key) # (votos, nome)
    candidatos.append(tupla)
candidatos.sort(reverse = True) # Ordem de votos decrescente

# Saída de dados

for candidato in candidatos:
    if candidato[1] != "Branco" and candidato[1] != "Nulo":
        # Printa "Nome Votos" para cada candidato
        print(candidato[1], urna[candidato[1]])

# Printa os votos brancos e nulos
print("Brancos", urna["Branco"])
print("Nulos", urna["Nulo"])