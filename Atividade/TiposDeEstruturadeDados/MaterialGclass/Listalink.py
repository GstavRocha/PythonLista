class No:
    def __init__(self, letra, prox):
        self.letra =letra
        self.prox = prox

lista = No('e',1), No('h',2),No('b',3),No('f',4),No('a',5),
No('i',6),No('g',7),No('c',8),No('d',-1)

l=0
while l != -1:
    print(lista[l].letra, end=',')
    l = lista[l].prox

class Lista:
    def inicio(self):
        
