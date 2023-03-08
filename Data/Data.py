class Data:
    limites = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
#Dicionário para indicar que o mês 2, possui 28 dias

    def __init__(self, dia:int, mes:int, ano:int):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    # ---- Acessadores ----

    @property
    def dia(self)-> int:
        return self.__dia
            
    @property
    def mes(self)-> int:
        return self.__mes

    @property
    def ano(self)-> int:
        return self.__ano

    # ---- Modificadores ----
    @dia.setter
    def dia(self, novoDia): 
        if novoDia >= 1 and novoDia <= 31:
            if self.__mes == 2 and novoDia <= Data.limites[2]:
                self.__dia = novoDia
            
            elif self.__mes != 2:
                    self.__dia = novoDia
            else:
                print("Formato de dia inválido")

    @mes.setter
    def mes(self, novoMes):
        if novoMes >= 1 and novoMes <= 12:
            if novoMes == 2 and self.__dia <= Data.limites[2]:
                self.__mes = novoMes
            elif novoMes != 2:
                self.__mes = novoMes
            else:
                print("Formato de mês inválido")
                

    @ano.setter
    def ano(self, novoAno):
        self.__ano = novoAno

    def __str__(self):
        return f'{self.__dia:02}/{self.__mes:02}/{self.__ano:02}'