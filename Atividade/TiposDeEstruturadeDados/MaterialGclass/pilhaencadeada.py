import sys
class Node:

    data = ''
    next = None
    
    def __init__(self, data):
        self.data = data


class Stack:
    top = None
    size = 0

    def isEmpty(self):
        return self.top == None
    
    def push(self,element):
        if self.isEmpty():
            self.top = Node(element)
        else:
            new_node = Node(element)
            new_node.next = self.top
            self.top = new_node
        self.size += 1
    
    def peek(self):
        return self.top
    
    def pop(self):
        if self.isEmpty():
            return None
        p = self.top
        self.top = self.top.next
        p.next = None
        self.size -= 1

        return p
    
    # def listItens(self):
    #     top = self.Node(self)
    #     print("Itens da Lista")
    #     for i in range(self.size):
    #         print(top[i])
    #         top = top.next

    def getSize(self):
        return self.size.len();        

def output(stack):
    print("Top ", end="")
    node = stack.pop()
    while node != None:
        print(node.data, " -> ", end="")
        node=stack.pop()
    print("End \n")

def main():
    stack = Stack()
    stack.push("A")
    stack.push("B")
    stack.push("C")
    stack.push("D")

    output(stack)
if __name__ == "__main__":
    main()

print("_________________")
stack = Stack()
stack.push("A")
stack.push("B")
stack.push("C")
stack.push("D")
stack.peek()
# stack.listItens()
