import Node;

class LinkedList:
    __head = None
    __tail = None

    def init(self):
        self.__head = Node("A",None)
        nodeB = Node("B",None)
        self._head.next = nodeB

        nodeC = Node("C",None)
        nodeB.next = nodeC

        self.__tail = ("D",None)
        nodeC.next = self.__tail

    @ property
    def head(self):
        return self.__head