P1 = float(input("Digite a nota da P1: ")) # Recebe a nota da P1
P2 = float(input("Digite a nota da P2: ")) # Recebe a nota da P2
P3 = float(input("Digite a nota da P3: ")) # Recebe a nota da P3

media = ((3 * P1) + (5 * P2) + (5 * P3)) / (3 + 5 + 5) # Calcula a média ponderada das provas com peso 3, 5 e 5, respectivamente

print(f"Media = {media:.2f}") # Printa a media das notas com 2 casas decimais
