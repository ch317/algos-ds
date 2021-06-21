from LinkedList import LinkedList, Node

#We will assume each data is repeated at most 2 times (1 duplicate)
def removeDuplicates(linkedList):

    listData = {}
    #1. Traverse the linkedlist
    current = linkedList.head
    if current == None:
        return linkedList

    #2. We store in a dict which are the duplicated data
    while current != None:
        if current.data in listData:
            listData[current.data] = True #It is a duplicated data, we store it
        else:
            listData[current.data] = False #It is not duplicated data, we store the key
        
        current = current.next
    
    #3. For each duplicated data, we remove it from the LinkedList using the method already implemented in LinkedList class
    for key, val in listData.items():
        if val is True:
            linkedList.remove(key)
    
    return linkedList



def test():
    node1 = Node(1)
    node2 = Node(2)
    node2Dup = Node(2)
    node3 = Node(3)
    linkedList = LinkedList()
    linkedList.add(node1)
    linkedList.add(node2)
    linkedList.add(node2Dup)
    linkedList.add(node3)
    linkedList.printList()
    linkedList = removeDuplicates(linkedList)
    linkedList.printList()

#Tests
test()