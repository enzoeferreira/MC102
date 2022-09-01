idade = int(input("Qual a idade? "))
estudante = input("É estudante? (S/N) ")

while not 0 <= idade <= 150:
    print("Idade inválida!")
    idade = int(input("Tente outra vez! Idade? "))

if 6 <= idade <= 60 and estudante == 'N':
    print("Paga tarifa.")
else:
    print("Gratuidade de tarifa.")