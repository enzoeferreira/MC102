n = int(input("Quantas pessoas serão digitadas? "))

alturas = {}
for i in range(n):
    nome = input(f"\nDigite o nome da {i + 1}a pessoa: ")
    altura = float(input("Digite a altura dessa pessoa: "))
    alturas[nome] = altura
    
print("\nAs alturas e nomes digitados são:")
for key in alturas:
    print(f"{key} tem {alturas[key]}m")