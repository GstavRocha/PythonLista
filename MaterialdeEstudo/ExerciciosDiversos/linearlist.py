class node:
    def __init__(self):
        self.data = ''
        self.next = None

    def __str__(self):
        return str(f"{self.data} -> {self.data}")

    @property
    def __repr__(self):
        return repr(f"{self.data} -> {self.data}")


# ListaLinear:

class linear_list:
    def __init__(self):
        self.elemento = None

    def is_empty(self):
        if linear_list is None:
            return print('Lista Vazia')

    def add(self, novoElemento):
        i = 0
        self.elemento = novoElemento
        if self.elemento > len():
            self.elemento.next = [i]novoElemento
            print(self.elemento.next)



teste = linear_list()
teste.add(2)
teste.is_empty()
