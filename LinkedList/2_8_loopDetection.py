from LinkedList import LinkedList, Node

def loopDetection(list):
    current = list.head

    nodes = {}
    while current != None:
        if current in nodes:
            return current
        
        nodes[current] = True
        current = current.next
    
    return None

def test():
    list1 = LinkedList() #A->B->Csamenode->D->E->Csamenode: we have a loop
    sameNode = Node("C")
    lastNode = Node("E")
    list1.add(Node("A"))
    list1.add(Node("B"))
    list1.add(sameNode)
    list1.add(Node("D"))
    list1.add(lastNode)
    lastNode.next = sameNode #We create the loop

    nodeLoop = loopDetection(list1)
    print(nodeLoop) #Node in the loop
    print(nodeLoop.data) #We confirm data is "C"

    list2 = LinkedList() #A->B->C->D->E->Cdifferentnode: no loop
    list2.add(Node("A"))
    list2.add(Node("B"))
    list2.add(Node("C"))
    list2.add(Node("D"))
    list2.add(Node("E"))
    list2.add(Node("C"))
    print(loopDetection(list2)) #None (there is no loop)

test()
