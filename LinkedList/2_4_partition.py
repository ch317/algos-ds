from LinkedList import LinkedList, Node

#Returns a linkedlist formed by concatenating list2 to list1
#This function assumes there is at least 1 element in every list
def mergeLists(list1, list2):

    current = list1.head
    #1. We traverse list1 to find the last element:
    while current.next != None:
        current = current.next
    
    current.next = list2.head

    return list1

def partition(linkedList, x):
    #1 We traverse the linkedlist and we add nodes with value < x to partition1 and nodes with value >= x to partition 2.
    # We are creating new nodes from the value of nodes of the original list in order to not have potential circular lists
    partition1 = LinkedList()
    partition2 = LinkedList()
    
    current = linkedList.head
    while current != None:
        newNode = Node(current.data)

        if current.data < x:
            partition1.add(newNode)
        else:
            partition2.add(newNode)
        
        current = current.next
    
    mergedList = mergeLists(partition1, partition2)
    return mergedList

def test():
    linkedList = LinkedList()
    linkedList.add(Node(3))
    linkedList.add(Node(5))
    linkedList.add(Node(8))
    linkedList.add(Node(5))
    linkedList.add(Node(10))
    linkedList.add(Node(2))
    linkedList.add(Node(1))
    partionList = partition(linkedList, 5)
    partionList.printList()

test()

    

