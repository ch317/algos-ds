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


#Trying to do it in one pass O(n) instead of one pass for every duplicated element O(N^2)
def removeDuplicates2(linkedList):
    if linkedList.head is None:
        return linkedList

    current = linkedList.head
    duplicatesDict = {}

    duplicatesDict[current.data] = True

    while (current.next != None):
        if current.next.data in duplicatesDict:
            current.next = current.next.next
        else:
            duplicatesDict[current.next.data] = True
            current = current.next
    
    return linkedList

#Trying to do without buffer. O(n^2)
def removeDuplicates3(linkedList):
    if linkedList.head is None:
        return linkedList

    p1 = linkedList.head

    while p1.next != None:
        p2 = p1.next
        while p2.next != None:
            if p2.data == p1.data:
                p1.next = p2.next
                p2 = p2.next
                continue

            if p2.next.data == p1.data:
                p2.next = p2.next.next
            else:
                p2 = p2.next

        if p1.next.next == None: #There remains 2 elements in the list
            if p1.data == p1.next.data: #2 elements are equal, we remove the last
                p1.next = None
                return linkedList
            else: #2 elements are different, we return the list as it is
                return linkedList
        
        p1 = p1.next
    
    return linkedList



def test1(linkedList):
    print("test1: removeDuplicates")
    linkedList = removeDuplicates(linkedList)
    linkedList.printList()

def test2(linkedList):
    print("test2: removeDuplicates2")
    linkedList = removeDuplicates2(linkedList)
    linkedList.printList()

def test3(linkedList):
    print("test2: removeDuplicates2")
    linkedList = removeDuplicates3(linkedList)
    linkedList.printList()

#Test 1
node1 = Node(1)
node2 = Node(2)
node2Dup = Node(2)
node3 = Node(3)
node3Dup = Node(3)
linkedList = LinkedList()
linkedList.add(node1)
linkedList.add(node2)
linkedList.add(node2Dup)
linkedList.add(node3)
linkedList.add(node3Dup)
print("Original list:")
linkedList.printList()
test1(linkedList)

#Test 2
node1 = Node(1)
node2 = Node(2)
node2Dup = Node(2)
node3 = Node(3)
node3Dup = Node(3)
linkedList = LinkedList()
linkedList.add(node1)
linkedList.add(node2)
linkedList.add(node2Dup)
linkedList.add(node3)
linkedList.add(node3Dup)
print("Original list:")
linkedList.printList()
test2(linkedList)

#Test 3
node1 = Node(1)
node2 = Node(2)
node2Dup = Node(2)
node2Dup2 = Node(2)
node3 = Node(3)
node3Dup = Node(3)
linkedList = LinkedList()
linkedList.add(node1)
linkedList.add(Node(1))
linkedList.add(node2)
linkedList.add(node2Dup)
linkedList.add(node2Dup2)
linkedList.add(node3)
linkedList.add(node3Dup)
linkedList.add(Node(3))
linkedList.add(Node(1))
print("Original list:")
linkedList.printList()
test3(linkedList)