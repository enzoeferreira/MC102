notas = [7.1, 10.0, 5.9, None, None]
diaDaSemana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]

for i in range(len(notas)):
    if notas[i] is None:
        print(f"{diaDaSemana[i]} não preenchida")

soma = 0.0
cont = 0

for i in range(len(notas)):
    if notas[i] is not None:
        soma += notas[i]
        cont += 1
        
print(f"Media das notas do RU: {(soma/cont):.2f}")