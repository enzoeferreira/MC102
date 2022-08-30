nome = input("Qual seu nome? ")
turma = input("Qual sua turma? ")

if turma == 'R':
    print(nome, ", sua sala é a SI03", sep="")
elif turma == 'S':
    print(nome, ", sua sala é a SI05", sep="")
else:
    print(nome, ", entre em ic.unicamp.br/~mc102", sep="")