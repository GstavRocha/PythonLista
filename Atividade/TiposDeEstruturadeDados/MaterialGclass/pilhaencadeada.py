class No:
    def __init__(self,dado):
        self.dado = dado
        self.next = None
    
    def __str__(self):
        return str(self.dado)
    
    def __repr__(self):
        return str(self.dado)

class PilhaEncadeada:
    def __init__(self):
        self.head = None
        self.tamanh = 0

    def is_empty(self):
        return self.head == None
    
    def push(self, novo):
        if self.is_empty():
            self.head = novo
        else:
            novo.next = self.head
            self.head = novo
        self.tamanh += 1
    def pop(self):
        if self.is_empty():
            return None
        else:
            pop = self.head
            self.head = self.head.next
            self.tamanh -= 1
            return pop
