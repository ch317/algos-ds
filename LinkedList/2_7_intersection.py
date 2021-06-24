from LinkedList import LinkedList, Node
#Returns if two lists intersects

#First solution, for each element in list1 we check if it is in list2 O(n1*n2)
def intersect(list1, list2):
    p1 = list1.head
    p2 = list2.head

    while p1 != None:
        while p2 != None:
            if p1 == p2:
                return True
            p2 = p2.next
        p1 = p1.next
        p2 = list2.head
    
    return False

#Second solution, we add every Node from list1 to a dict as key and check if a node from list2 is in the dict
def intersect2(list1, list2):

    p1 = list1.head
    nodes1 = {}
    while p1 != None:
        nodes1[p1] = True
        p1 = p1.next
    
    p2 = list2.head
    while p2 != None:
        if p2 in nodes1:
            return True
        p2 = p2.next

    return False

def test1():
    nodeIntersection = Node(4)
    list1 = LinkedList() #7->1->4intersect
    list1.add(Node(7))
    list1.add(Node(1))
    list1.add(nodeIntersection)
    list2 = LinkedList() #5->9->4intersect
    list2.add(Node(5))
    list2.add(Node(9))
    list2.add(nodeIntersection)
    print(intersect(list1, list2)) #True

    list1 = LinkedList() #7->1->4 without intersection at node reference
    list1.add(Node(7))
    list1.add(Node(1))
    list1.add(Node(4))
    list2 = LinkedList() #5->9->4 without intersection at node reference
    list2.add(Node(5))
    list2.add(Node(9))
    list2.add(Node(4))
    print(intersect(list1, list2)) #False

test1()

def test2():
    nodeIntersection = Node(4)
    list1 = LinkedList() #7->1->4intersect
    list1.add(Node(7))
    list1.add(Node(1))
    list1.add(nodeIntersection)
    list2 = LinkedList() #5->9->4intersect
    list2.add(Node(5))
    list2.add(Node(9))
    list2.add(nodeIntersection)
    print(intersect2(list1, list2)) #True

    list1 = LinkedList() #7->1->4 without intersection at node reference
    list1.add(Node(7))
    list1.add(Node(1))
    list1.add(Node(4))
    list2 = LinkedList() #5->9->4 without intersection at node reference
    list2.add(Node(5))
    list2.add(Node(9))
    list2.add(Node(4))
    print(intersect2(list1, list2)) #False

test2()