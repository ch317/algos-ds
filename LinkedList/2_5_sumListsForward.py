from LinkedList import LinkedList, Node
#Same as 2.5 but assuming lists are forward:
# 6->1->7 represents 617
from reverseList import reverseList


def sumNodes(p1, p2):
    #Base case
    if p1 is None:
        return (0, LinkedList())

    carry, sumList = sumNodes(p1.next, p2.next)
    sum = p1.data + p2.data + carry
    unit = sum%10
    sumList.add(Node(unit))

    if sum >= 10:
        return (1, sumList)
    
    return (0, sumList)

#We assume that lists are equal length
def sumListsForward(list1, list2):
    carry, sumList = sumNodes(list1.head, list2.head)
    
    if carry == 1:
        sumList.add(Node(1))
    
    return reverseList(sumList)

#Test1
list1 = LinkedList() #6->1->7
list1.add(Node(6))
list1.add(Node(1))
list1.add(Node(7))
list2 = LinkedList() #7->5->4
list2.add(Node(7))
list2.add(Node(5))
list2.add(Node(4))

sumList = sumListsForward(list1, list2)
sumList.printList() #1->3->7->1

#Test2
list1 = LinkedList() #1->1->2
list1.add(Node(1))
list1.add(Node(1))
list1.add(Node(2))
list2 = LinkedList() #2->2->3
list2.add(Node(2))
list2.add(Node(2))
list2.add(Node(3))

sumList = sumListsForward(list1, list2)
sumList.printList() #3->3->5