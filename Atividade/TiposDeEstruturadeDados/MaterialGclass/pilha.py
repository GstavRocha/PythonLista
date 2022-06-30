#https://docs.python.org/pt-br/3/tutorial/datastructures.html
# pilha = [1,2,3,4,5,6,7,8,8]
# pilha.append(10)
# print(pilha)
# pilha.pop(0) # Nesse caso se o pop for vazio ele deleta o ultimo elemento que entrou.
# # como foi apontando ele deletou o indice indicado.
# print(pilha)

class Pilha:
    def __init__(self):
        self.pilha = []
    
    def is_empty(self):
        if self.pilha == []:
           return self.pilha
        else:
           print('A lista não está vazia')
    
    def push(self,valor):
        return self.pilha.append(valor)
    def pop(self):
        return self.pilha.pop()
    
    def peek(self):
        return self.pilha[len(self.pilha)-1]
    
    def list_items(self):
        for i in self.pilha:
            print(i)

teste = Pilha()
teste.push('1')
teste.push('2')
teste.push('4')
teste.push('5')
teste.push('6')
teste.push('7')
teste.list_items()
teste.is_empty()