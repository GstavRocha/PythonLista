class Animal:
    def __init__(self,peso,nome,posicao):
        self.peso =peso
        self.nome =nome
        self.posicao = posicao
    
    def moverse(self):
        self.posicao +=1
        print(self.posicao)
    
    def local (self):
        return self.posicao
    def latir(self):
        print("Au,au...")

gustavo = Animal(25,'Lucky',1)
gustavo.moverse()
gustavo.moverse()
gustavo.moverse()
gustavo.moverse()
gustavo.moverse()
gustavo.moverse()
gustavo.moverse()
gustavo.moverse()
gustavo.latir()
gustavo.latir()
gustavo.latir()
gustavo.latir()
gustavo.latir()
gustavo.latir()
