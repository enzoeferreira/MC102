try:
    x = int(input("Digite um inteiro para x: "))
except:
    print("Digite um número inteiro, por favor.")

try:
    y = int(input("Digite um inteiro para y: "))
except:
    print("Digite um número inteiro, por favor.")

try:
    print(f"x + y = {x+y}")
except:
    print("Erro.")