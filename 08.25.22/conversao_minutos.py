from tkinter import N


n = int(input())
horas = n // 60
minutos = n % 60

print(horas, "h", minutos, "min", sep="")

""""
Outra forma de printar seria
print(f"{horas}h{minutos}min)
""" 