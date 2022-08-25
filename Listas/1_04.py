"""
Faça um programa que leia dois valores inteiros nas variáveis x e y e troque o conteúdo
das variáveis. Por exemplo, supondo que x = 2 e y = 10 foram os valores lidos, o seu
programa deve fazer com que x = 10 e y = 2. Refaça este problema usando apenas x e y
como variáveis.
"""

x = int(input("X = "))
y = int(input("Y = "))

x, y = y, x

print(f"\nX = {x}")
print(f"Y = {y}")
