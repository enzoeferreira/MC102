animais = ["galo", "cobra", "gato", "lontra"]

"""
Prints de cada elemento
"""

print(animais[3]) # Saída: lontra

i = 1

print(animais[i]) # Saída: cobra

i += 1

print(animais[i]) # Saída: gato

"""

"""

animais[0] = "hiena"
print(animais) # ["hiena", "cobra", "gato", "lontra"]

i = 0

while i < len(animais):
    if animais[i] == "cobra":
        animais[i] = "lebre"
    i += 1

print(animais) # ["hiena", "lebre", "gato", "lontra"]