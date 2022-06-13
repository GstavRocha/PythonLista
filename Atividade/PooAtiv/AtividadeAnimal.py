
class Animal:
    def __init__(self, peso, nome, posicao):
        self._peso = peso
        self._nome = nome
        self._posicao = posicao

    def moverse(self):
        self._posicao +=1
        # print(self._posicao)
    def local(self):
        return self._posicao

class Gato(Animal):
    def __init__(self, peso, nome, posicao,naArvore):
        self._naArvore = naArvore
        super().__init__(peso,nome,posicao)
    
    def miar(self):
        print('Miauuu...')
    
    def estar_arvore(self):
        if self._naArvore == True:
            return 'Está na Árvore'
        else:
            return 'Não está na Árvore'
    
    def subir_arvore(self):
        if self._naArvore == True:
            return 'Já está na Arvore'
        else: 
            self._naArvore = True
            return "Subiu na arvore"
    def descer_arvore(self):
        if self.estar_arvore == True:
            self.estar_arvore == False
            return "Desceu da Arvore"
        else:
            return "Ele já está embaixo"

class Cachorro(Animal):
    def __init__(self,peso, nome, posicao, qtd_saltos):
        self._qtd_saltos = qtd_saltos
        super().__init__(peso,nome, posicao)
    
    def latir(self):
        print ('Au, au...')
    def saltar(self):
        self._qtd_saltos += 1
    def descansar(self):
        self._qtd_saltos = 0

    def esta_cansado(self):
        if self._qtd_saltos > 5:
            print('Está cansado')
            return True
        else:
            contarSaltos = 5 - self._qtd_saltos
            print( f'Ele ainda tem {contarSaltos} de saltos')

chanim = Gato(10,"Chanim",2,False)
lucky = Cachorro(25,'Lucky',2,2)
