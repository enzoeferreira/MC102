from tkinter import N


n = int(input())    # Recebe a quantidade de minutos
horas = n // 60     # Divisão inteira de minutos por 60
minutos = n % 60    # Resto da divisão inteira

print(horas, "h", minutos, "min", sep="") # Printa o tempo em horas/minutos no formato XhYmin

""""
Outra forma de printar seria
print(f"{horas}h{minutos}min)
""" 