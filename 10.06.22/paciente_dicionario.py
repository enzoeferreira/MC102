paciente = {}
paciente["Idade"] = 39
paciente["Altura"] = 1.81
paciente["Glicemia"] = 300

print(paciente)

for chave in paciente:
    print(chave)

for chave in paciente:
    print(f"{chave} = {paciente[chave]}")