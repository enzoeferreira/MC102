quantidade = int(input("Quantas temperaturas serão lidas? "))
temperaturas = []

for _ in range(quantidade):
    temp = float(input())
    temperaturas.append(temp)

print(temperaturas)

print("Temperaturas em ordem crescente:")
temperaturas.sort()
print(temperaturas)

print("Média das temperaturas:", sum(temperaturas)/len(temperaturas))