# Igual ao código de nome semelhante, mas utilizando pi importado da biblioteca math

from math import pi

forca = float(input("DIgite a força (em N): "))  # Recebe o número racional da força
raio = float(input("Digite a força (em m): "))   # Recebe o número racional do raio

area = pi * (raio ** 2) # Calcula a àrea (pi)r²
pressao = forca / area  # Calcula a pressão

print(f"{pressao:.2f} Pa") # Printa a pressão no formato "X Pa" com 2 casas decimais

# print(pressao, "Pa")    # Printa a pressão no formato "X Pa"

"""
Outra forma de printar seria
print(f"{forca/area} Pa")
"""