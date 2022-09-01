try:
    nota = float(input("Digite sua nota: "))
except:
    print("A entrada precisa ser um número.")
    exit(0)

# if 0 <= nota <= 10:
if nota >= 0 and nota <= 10:
    print("Status:", end=" ")
    if nota < 2.5:
        print("Reprovado.")
    elif nota < 5.0:
        print("Exame.")
    else:
        print("Aprovado.")
else:
    print("Entrada Inválida")
