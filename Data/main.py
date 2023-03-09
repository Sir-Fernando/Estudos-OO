from Data import Data

import os
os.system("cls")

hoje = Data(9, 3, 2023)

dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))

hoje.dia = dia
hoje.mes = mes
hoje.ano = ano

print(hoje)
