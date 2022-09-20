quantidade = int(input("Quantas temperaturas serão lidas? "))
temperaturas = []

for _ in range(quantidade):
    temperaturas.append(float(input("Digite uma temperatura: ")))

print("Temperaturas em ordem crescente:")
temperaturas.sort()

print(temperaturas)
print("Média das temperaturas:", sum(temperaturas)/len(temperaturas))
print("Temperatura Max:", max(temperaturas), "°C")
print("Temperatura Min:", min(temperaturas), "°C")