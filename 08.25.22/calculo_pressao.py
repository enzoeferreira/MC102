forca = float(input())
raio = float(input())

pi = 3.14159265

area = pi * (raio ** 2)
pressao = forca / area

print(pressao, "Pa")

"""
Outra forma de printar seria
print(f"{forca/area} Pa")
"""