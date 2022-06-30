# Etendendo o funcionamento de repr

class Pessoa:
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade
    
    def __repr__(self):
        representa = 'Pessoa('+ self.nome +','+ str(self.idade) +')'
        return representa
        
    

pessoa = Pessoa("Gustavo", 37)


