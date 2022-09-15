animais = ["galo", "cobra", "gato", "lontra"]

"""
Todos os jeitos de escrever são equivalentes em resultado
"""

# Método 1
i = 0
while i < len(animais): # Tbm é valido i < 4 (se souber o tamanho da lista)
    print(animais[i])
    i += 1

# Método 2
for i in range(len(animais)):
    print(animais[i])
    i += 1

# Método 3 (O "melhor")
for animal in animais:
    print(animal)