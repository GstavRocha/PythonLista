class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(f"{self.data} -> {self.data} ")

    def __repr__(self):
        return repr(f"{self.data} -> {self.data}")


class ListaCiruclar:
    def __init__(self, no=None):
        # self.head = head
        self.size = 0
        self.tail = no

    def is_empty(self):
        if self.size == 0:
            return print('Lista Vazia')

    def append(self, element):
        if element is None:
            return self.is_empty()
        else:
            newnode = Node(element)
            self.tail = newnode
            newnode.next = self.tail
            self.size += 1
            return print(Node(element), end=' - > ')


teste = ListaCiruclar()
teste.append(2)
teste.append(3)
teste = ListaCiruclar()
