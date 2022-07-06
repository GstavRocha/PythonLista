from lista_ligada import *

def output(node):
    p = node
    while (p != None):
        data = p.data
        print(data, "-> ",end="")
    print("End\n\n")

def main():
   linkedlist = LinkedList()
   linkedlist.init()
   output(linkedlist.head)

if __name__== "__main__":
    main()