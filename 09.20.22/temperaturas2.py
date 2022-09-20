quantidade = int(input("Quantas temperaturas serão lidas? "))
temperaturas = []

for _ in range(quantidade):
    temperaturas.append(float(input("Digite uma temperatura: ")))

print("Temperaturas em ordem crescente:")
temperaturas.sort()

print(temperaturas)
media = sum(temperaturas)/len(temperaturas)
print("Média das temperaturas:", media)
print("Temperatura Max:", max(temperaturas), "°C")
print("Temperatura Min:", min(temperaturas), "°C")

# Cálculo do Desvio Padrão Amostral
n = len(temperaturas)
soma = 0
for i in range(len(temperaturas)):
    soma += (temperaturas[i] - media) ** 2
desvio_padrao = (soma / (n - 1)) ** 0.5

print("Desvio padrão:", desvio_padrao)