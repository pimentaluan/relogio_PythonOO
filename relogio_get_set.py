class Relogio:
    def __init__(self, hora, minuto, segundo):
        self.__hora = hora
        self.__minuto = minuto
        self.__segundo = segundo
    
    def get_hora_formatada(self):
        #12:34:36
        return f'{self.__hora:02d}:{self.__minuto:02d}:{self.__segundo:02d}'
        
    def get_hora(self):
        #12
        return self.__hora
    
    def get_minuto(self):
        #34
        return self.__minuto
        
    def get_segundo(self):
        #36
        return self.__segundo
    
    def set_hora(self, novo_valor):
        if novo_valor < 24:
            self.__hora = novo_valor
        else:
            print('Adicione um número entre 0 e 24')
    
    def set_minuto(self, novo_valor):
        if novo_valor < 60:
            self.__minuto = novo_valor
        else:
            print('Adicione um número entre 0 e 59')

    def set_segundo(self, novo_valor):
        if novo_valor < 60:
            self.__segundo = novo_valor
        else:
            print('Adicione um número entre 0 e 59')
        
    def adicionar_hora(self, adc):
        self.__hora = (self.__hora + adc) % 24

    def adicionar_minuto(self, adc):
        self.adicionar_hora((self.__minuto + adc) // 60)
        self.__minuto = (self.__minuto + adc) % 60

    def adicionar_segundo(self, adc):
        self.adicionar_minuto((self.__segundo + adc) // 60)
        self.__segundo = (self.__segundo + adc) % 60

    def subtrair_hora(self, sub):
        self.__hora = (self.__hora - sub) % 24

    def subtrair_minuto(self, sub):
        self.subtrair_hora(sub // 60)
        self.__minuto = (self.__minuto - sub) % 60

    def subtrair_segundo(self, sub):
        self.subtrair_minuto(sub // 60)
        self.__segundo = (self.__segundo - sub) % 60
        
if __name__ == '__main__':
    relogio = Relogio(12, 34, 36)
    print(relogio.get_hora_formatada())

    relogio.adicionar_hora(1)
    relogio.adicionar_minuto(40)
    relogio.adicionar_segundo(40)
    print(relogio.get_hora_formatada())

    relogio.subtrair_hora(2)
    relogio.subtrair_minuto(6)
    relogio.subtrair_segundo(40)
    print(relogio.get_hora_formatada())