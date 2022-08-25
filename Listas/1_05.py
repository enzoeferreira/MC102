"""
Faça um programa que leia os valores correspondentes aos três lados a, b e c de um triângulo.
O programa então deve determinar se o triângulo é isósceles, escaleno ou equilátero,
informando isto para o usuário, e em seguida o programa deve imprimir a área A do
triângulo utilizando a fórmula de Heron:
A = raiz(s*(s-a)*(s-b)*(s-c)) ; onde s = (a+b+c)/2
"""

a = float(input("Digite o valor do lado a: "))
b = float(input("Digite o valor do lado b: "))
c = float(input("Digite o valor do lado c: "))

if a == b == c:
    print("\nTriangulo Equilatero")
elif (a==b and a != c) or (a==c and a != b) or (c == b and c != a):
    print("\nTriangulo Isosceles")
else:
    print("\nTriangulo Escaleno")

s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** (1/2)

print(f"Area = {area}")

