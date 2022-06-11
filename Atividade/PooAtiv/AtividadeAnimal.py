# Implemente as classes conforme diagrama UML (SLIDE);
# O método esta_cansado() retorna true quando o cachorro tiver dado mais do 5 saltos.
# O método descansar() zera os saltos do  Cachorro.
# O método esta_na_arvore() retorna o valor do atributo naArvore
# Os metodos latir() e miar() devem escrever na tela as mensagens relativas aos sonos.
# O metodo construto das subclasses deve parametrizar o nome e o peso.

class Animal:
    def __init__(self, peso, nome, posicao):
        self._peso = peso
        self._nome = nome
        self._posicao = posicao

    def moverse(self):
        self._posicao +=1
        print(self._posicao)

class Gato(Animal):
    def __init__(self):
      self.naArvore = true
    
    def miar(self):
        print ('Miauu....')
    
    def subirNArvore(self):
        self.posicao += 1
    def descerArvore(self):
        self.posicao -= 1
    def estarNArvore(self):
        if Gato.subirNArvore > 5:
            return Gato.miar()

mixano = teste