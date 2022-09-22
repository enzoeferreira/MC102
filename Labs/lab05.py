##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Jornada de Trabalho
# Nome: Enzo Emidio Ferreira
# RA: 243161
##################################################

# Leitura do valor da hora
V = int(input())

# Leitura do numero de dias trabalhados na semana
D = int(input())

# Leitora e processamento dos periodos de trabalho de cada dia

horasTrabDiaria = []
horasExtrasDiarias = 0
for i in range(D):
    horasTrab = 0
    periodo = int(input())
    
    j = 0
    while j < periodo:
        start = int(input())
        stop = int(input())
        
        horasTrab += (stop - start)
        
        j += 1
    if horasTrab > 8:
        horasExtrasDiarias += horasTrab - 8
        print(f"horas extras = {horasExtrasDiarias}")
    horasTrabDiaria.append(horasTrab)

# Calculo do valor devido ao funcionário

horasExtras = 0

valor = (V * sum(horasTrabDiaria))
if sum(horasTrabDiaria) > 44:
    horasExtras += sum(horasTrabDiaria) - 44
    print(horasExtras)
    horasExtras += horasExtrasDiarias
    print(horasExtras)
if horasExtras > 0:
    valor += ((V/2) * horasExtras)

# Impressão da saída
print("Horas trabalhadas:", sum(horasTrabDiaria))
print("Horas extras:", horasExtras)
print("Valor devido: R$ {:0.2f}".format(valor))