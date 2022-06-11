class teste:
    #para acessar os elementos de uma classe pode-se usar ponto. entre o nome da calss e  o elemento da class.
    x = "Gustavo"

class Pessoa:
    def __init__(self,name,age):
        self.name = name
        self.age = age

pessoa = Pessoa('Gustavo',36)

print(pessoa.name)
print(pessoa.age)

#Métodos são objetos que possuem funções. Tais funções pertencem ao objeto.
class Pessoa2:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def minhafuncao(self):
        print(" Testando o ",self.name)
        print("Idade é ",self.age)
p2 = Pessoa2("Gustavo",37)
p2.minhafuncao()

# o sefl serve para acessar as variáveis das classes. Mas pode ser usando outro nome para acessar as mesmas.
# Contudo deve-se obdecer a ideia que o primeiro parametro serve para acessar as variáveis.

#exemplo:
class Testa:
    def __init__(queijo,exemplo, festa):
        queijo.exemplo = exemplo
        queijo.festa = festa
    def printa(leite):
        print(' Testando',leite.exemplo)
        print(' o segundo',leite.festa)
p3 = Testa('chinelo','são joão')
p3.printa()