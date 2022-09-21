##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Jornada de Trabalho
# Nome: Enzo Emidio Ferreira
# RA: 243161
##################################################

# Leitura do valor da hora
V = int(input("Valor da hora de trab: "))

# Leitura do numero de dias trabalhados na semana
D = int(input("Dias de trabalho: "))

# Leitora e processamento dos periodos de trabalho de cada dia

horasTrabalhadas = 0
for i in range(D):
    periodo = int(input(f"Periodos do dia {i + 1}: "))
    print(periodo)
    
    j = 0
    while j < periodo:
        start = int(input(f"Começo do periodo {j + 1}: "))
        stop = int(input(f"Fim do periodo {j + 1}: "))
        
        horasTrabalhadas += (stop - start)
        
        j += 1

# Calculo do valor devido ao funcionário



# Impressão da saída
print("Horas trabalhadas:", horasTrabalhadas)
# print("Horas extras:", horasExtras)
# print("Valor devido: R$ {:0.2f}".format(valor))