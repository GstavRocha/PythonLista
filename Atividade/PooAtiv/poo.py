# class Pessoa:
#     def __init__(self,nome, idade):
#         self.nome = nome
#         self.idade = idade
#     def dizerNome(self):
#         print('Meu nome é {}'.format(self.nome))
# p1 = Pessoa('Gustavo',37)
class Animal:
    def __init__(self, peso, nome, posicao):
        self.peso = peso
        self.nome = nome
        self.posicao = posicao
    def moverse(self):
        self.posicao += 1
    def local(self):
        return self.posicao

class Gato(Animal):
    def __init__(self,peso,nome, posicao):
        super().__init__(self,peso,nome,posicao)
        
        def miar(self):
            print('Miau...')
class Cachorro(Animal):
    def __init__(self, peso, nome, posicao):
        super().__init__(peso, nome, posicao)
        def latir (self):
            print('Au ,Au...')


lucky = Animal(35,'Lucy',3)
coco = Cachorro(25,'Cocada',2)

coco.posicao(2)
print(coco.__init__())