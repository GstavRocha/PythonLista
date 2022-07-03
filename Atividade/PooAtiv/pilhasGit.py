from dataclasses import dataclass


class No:
    def __init__(self,data):
        self.data = data
        self.next = None

        def __str__(self):
            return str(self.data)
        
        def __repr__(self):
            return str(self.data)
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def isEmpty(self):
        return self.top == None
    
    def push(self, element):
        if self.isEmpty():
            self.top = No(element)# Adcionar o No aqui
        else:
            newNode = No(element)
            newNode.next = self.top
            self.top = newNode
        self.size += 1
    
    def pop(self):
        if self.isEmpty():
            return None
        p = self.top
        self.top = self.top.next
        self.size -= 1
        return p
    
    def peek(self):
        return self.top

    def listItens(self):
        top = self.top
        print("Exibindo intes da lista")
        for i in range(self.size):
            print(top)
            top = top.next
    def getSize(self):
        return self.size

stack = Stack()
stack.push("A")
stack.push("B")
stack.push("C")
stack.push("D")
stack.listItens()



