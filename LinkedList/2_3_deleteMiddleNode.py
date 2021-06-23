from LinkedList import LinkedList, Node

#Solution 1
def deleteMiddleNode(linkedList, node):
    #1 We find the node to delete by traversing the list
    prev = linkedList.head
    current = prev.next

    #2 We remove the node from the list if found. NOt required to check edge case of head==nodeToDelete since
    # problem statement says nodeToDelete is in the middle of the list.
    while current != None:
        if current == node:
            prev.next = current.next
            return linkedList
        
        current = current.next
        prev = prev.next
    
    return linkedList


#Solution 2
#We traverse the list using recursion returning a node in each call. If the returned node by the call
#is the node to delete, then we delete that node from the list.
#Since the list will only have one node to delete, only 1 call will return that node (assuming it is on the list)
def deleteMiddleNode2(node, nodeToDelete):

    if node == None:
        return None

    nextNode = deleteMiddleNode2(node.next, nodeToDelete)
    if nextNode == nodeToDelete:
        node.next = nextNode.next

    return node

def test1():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    linkedList = LinkedList()
    linkedList.add(node1)
    linkedList.add(node2)
    linkedList.add(node3)
    linkedList.printList() #print 1 2 3

    linkedList = deleteMiddleNode(linkedList, node2)
    linkedList.printList() #print 1 3

def test2():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    linkedList = LinkedList()
    linkedList.add(node1)
    linkedList.add(node2)
    linkedList.add(node3)
    linkedList.printList() #print 1 2 3

    deleteMiddleNode2(linkedList.head, node2)
    linkedList.printList() #print 1 3

test1()
test2()