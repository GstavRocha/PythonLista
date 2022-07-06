from requests import head
from Node import Node

class SingleCircleLink:
    __head = None
    __tail = None
    def init(self):
        self.__head = Node("A")
        self.__head.next = None
        
        nodeB = Node("B")
        nodeB.next = None
        self.__head.next = nodeB

        nodeC = Node("C")
        nodeC.next = None
        nodeB.next = nodeC

        self.__tail = Node("D")
        self.__tail.next = self.__head
        nodeC.next = self.__tail
    
    def isEmpty(self):
        if self.head == None:
            print( "Lista está vazia")
        else:
            print("Lista não está vazia")
    
    def insert(self,element,newNode):
        p = self.__head
        i = 0
        while (p.next != None and i < element-1):
            p = p.next
            i += 1

            newNode.next = p.next
            p.next = newNode
    
    def remove(self, removePosition):
        p = self.__head
        i = 0
        while(p.next != None and i < removePosition-1):
            p = p.next
            i += 1
            temporary = p.next
            p.next = p.next.next
            temporary.next = None

    @property
    def head(self):
        return self.__head
