#FUNCIONOU

class Node:
    data = ''
    next = None
    def __init__(self,data,next):
        self.data = data
        self.next = next

class LinkList:
    head = None
    tail = None

    def init(self):
        self.head = Node("A",None)

        nodeB=Node("B",None)
        self.head.next=nodeB

        nodeC=Node("C",None)
        nodeB.next=nodeC

        self.tail=Node("D",None)
        nodeC.next=self.tail

    def add(self,new):
        self.tail.next = new
        self.tail = new
        
    
def output(node):
    p = node
    while(p!=None):
        data = p.data
        print(data,"-> ",end="")
        p=p.next
    print("End\n\n")

def main():
    linkedlist = LinkList()
    linkedlist.init()
    linkedlist.add(Node("E",None))
    output(linkedlist.head)

if __name__=="__main__":
    main()

