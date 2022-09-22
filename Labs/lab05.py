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

horasDiarias = []
horasExtras = []
for dia in range(D):
    horasTrabalhadas = 0
    
    periodos = int(input())
    for periodo in range(periodos):
        start = int(input())
        stop = int(input())
        
        horasTrabalhadas += stop - start
    horasDiarias.append(horasTrabalhadas)
    horasExtras.append(horasTrabalhadas - 8) if horasTrabalhadas > 8 else horasExtras.append(0)

# Calculo do valor devido ao funcionário

cargaHoraria = sum(horasDiarias)
cargaExtra = sum(horasExtras)

if cargaHoraria - cargaExtra > 44:
    cargaExtra += (cargaHoraria - cargaExtra) - 44

valor = (V * cargaHoraria) + ((V/2) * cargaExtra)

# Impressão da saída
print("Horas trabalhadas:", cargaHoraria)
print("Horas extras:", cargaExtra)
print("Valor devido: R$ {:0.2f}".format(valor))