import pandas
import numpy ?

df = pandas.read_excel('planilha.xls') # cria um dataframe com a planilha
df = pandas.read_excel('planilha.xls', usecols='A,C' ou 'A:C')
# pega só as colunas A e C (1°) ou de A a C (2°)

df.plot() # Plota em um grafico o dataframe (matplotlib)
df.describe() # Mostra as estatisticas gerais (min/max, media, quantidade...)

df.head() # primeiras linhas
df.tail() # ultimas linhas

import numpy

numpy.array([3.14, 2.7, 1.4])

array.astype(str) # Converte o array para string
array.astype(int) # Converte o array para inteiro
array.tolist() # Converte em lista do python

x = numpy.array(input().split()).astype(float).tolist() # mucha coisa