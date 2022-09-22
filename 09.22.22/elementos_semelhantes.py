listaA = [3, 5, 9, 1, 2, 3]
listaB = [8, 9, 0, 5, 6, 3]

repetidos = []

for itemA in listaA:
    if itemA in listaB and itemA not in repetidos:
        repetidos.append(itemA)

print(f"Há {len(repetidos)} elementos repetidos:")
print(*repetidos)