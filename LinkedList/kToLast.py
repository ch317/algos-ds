from LinkedList import LinkedList, Node

#O(n) We do two passes, first to count the number of elements and second to retrieve the kToLast
def kToLast(linkedList, k):
    #1. Traverse the list to know its length:
    n = 0
    current = linkedList.head

    if current == None:
        return None
    
    while (current != None):
        n = n + 1
        current = current.next

    if k > n:
        return None

    elementKToLast = n - k
    current = linkedList.head
    for i in range(elementKToLast):
        current = current.next
    
    return current

#Solution using recursion. Just in one pass. Time = O(n) Space = O(n) due to stack increasing for every recursive call
def getKToLastNode(node, kToLast):
    if node.next is None:
        return (node, 1)
    
    nodeNext, countFromLast = getKToLastNode(node.next, kToLast)

    if countFromLast == kToLast: #if this happes nodeNext is the node we want to return in every call
        return (nodeNext, countFromLast)

    countFromLast += 1
    return (node, countFromLast)

    
def kToLast2(linkedList, k):
    node, countFromLast = getKToLastNode(linkedList.head, k)
    return node


#Test 1
def test1():
    linkedList = LinkedList()
    linkedList.add(Node(1))
    linkedList.add(Node(1))
    linkedList.add(Node(2))
    linkedList.add(Node(2))
    linkedList.add(Node(2))
    linkedList.add(Node(3))
    linkedList.add(Node(3))
    linkedList.add(Node(1))
    print("Original list:")
    linkedList.printList()
    k = 2
    print("k to Last Element: " + str(k))
    node = kToLast(linkedList, k)
    if node is None:
        print("Insert k < n")
    else:
        print(node.data)
#test1()

#Test 2
def test2():
    linkedList = LinkedList()
    linkedList.add(Node(1))
    linkedList.add(Node(1))
    linkedList.add(Node(2))
    linkedList.add(Node(3))
    print("Original list:")
    linkedList.printList()
    node = kToLast2(linkedList, 4)
    print(node.data)

test2()