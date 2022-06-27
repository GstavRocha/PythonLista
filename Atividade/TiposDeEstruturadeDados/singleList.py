class No:
    dado = ''
    prox = None
    def __init__(self,dado,prox):
        self.dado = dado
        self.prox = prox

class ListaVinculada:
    __head = None
    __tail = None

    def __init__(self):
        self.__head = No("A",None)
        noB = No('B',None)
        self.__head.prox = noB
        noC = No('C', None)
        noB.prox = noC
        self.__tail = No('D',None)
        noC.next = self.__tail
    
    @property
    def head(self):
        return self.__head
