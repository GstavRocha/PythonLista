class No:
    def __init__(self, letra, prox):
        self.letra =letra
        self.prox = prox
    
    def __repr(self):
        return '% -> % ', (self.letra,self.prox)

lista = [No('e',5), No('h',2),No('b',2),No('f',6),No('a',1),
No('i',8),No('g',7),No('c',3),No('d',4)]

l= 0
while l <= 8:
    print(lista[l].letra, end='')
    l=lista[l].prox
    l += 1


        
