from Data import Data

import os
os.system("cls")

dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))

hoje = Data(dia, mes, ano)

#hoje.dia = dia
#hoje.mes = mes
#hoje.ano = ano

print(hoje)
