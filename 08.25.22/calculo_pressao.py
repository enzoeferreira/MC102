forca = float(input())  # Recebe o número racional da força
raio = float(input())   # Recebe o número racional do raio

pi = 3.14159265 # Pi constante, é possível colocar uma biblioteca matemática

area = pi * (raio ** 2) # Calcula a àrea (pi)r²
pressao = forca / area  # Calcula a pressão

print(pressao, "Pa")    # Printa a pressão no formato "X Pa"

"""
Outra forma de printar seria
print(f"{forca/area} Pa")
"""