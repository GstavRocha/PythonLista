# Nó
class Node:
    def __init__(self, data=''):
        self.data = data
        self.next = None

    def __str__(self):
        return str(f"{self.data} - > {self.data}")

    @property
    def __repr__(self):
        return repr(f"{self.data} -> {self.data}")


# ListaCircularLinkada

class LinkedList:
    def __init__(self, head):
        self._head = head
        self._tail = None

    def is_empty(self):
        print('Lista Vazia')
        return self._tail is None

    def add(self, newnode):
        if LinkedList is None:
            newnode.next = None
            self._head = newnode
            return self.is_empty()

        elif newnode <= self._head:
            newnode.next = self._head
            self._head = newnode


teste = LinkedList(2)
teste.add(1)
