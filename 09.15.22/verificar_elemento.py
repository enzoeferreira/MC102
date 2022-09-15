n = int(input("Quantos números serão lidos? "))
listas = []

for _ in range(n): # Usa-se "_" como o nome da var caso ela não será usada
    x = int(input("Digite um número: "))
    listas.append(x)

verify = int(input("Qual número devo verificar? "))

if verify in listas:
    print(verify, "esta na lista")
else:
    print(verify, "não está na lista")