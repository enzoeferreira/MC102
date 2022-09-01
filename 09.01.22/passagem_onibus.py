idade = int(input("Qual a idade? "))

if idade > 0 and idade < 150:
    if idade >= 6 and idade < 60:
        print("Paga tarifa.")
    else:
        print("Gratuidade de tarifa.")
else:
    print("Idade inválida.")