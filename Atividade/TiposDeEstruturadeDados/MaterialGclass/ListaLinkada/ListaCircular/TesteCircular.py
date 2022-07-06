from Node import Node
from Lista_circular import SingleCircleLink

def output(head):
    p = head
    print(p.data," -> ",end="")
    p = p.next

    while(p != head):
        
        print(p.data," -> ",end="")
        p = p.next

    print(p.data,"\n\n")
def main():
    circleLink = SingleCircleLink()
    circleLink.init()
    circleLink.isEmpty()
    circleLink.insert(2,Node("E"))
    circleLink.insert(2,Node("F"))
    circleLink.remove(2)



    output(circleLink.head)
if __name__ == "__main__":
    main()