from LinkedList import LinkedList, Node

def reverse(list, node):

    if node.next is None:
        list.head = node
        return node

    nextNode = reverse(list, node.next)
    nextNode.next = node
    return node

def reverseList(list):

    lastNodeReversedList = reverse(list, list.head) #This function changes the list variable already and returns last node of new reversed list
    lastNodeReversedList.next = None
    return list


#Tests
list = LinkedList() #1->5->7->9
list.add(Node(1))
list.add(Node(5))
list.add(Node(7))
list.add(Node(9))

reversedList = reverseList(list)
reversedList.printList() #9->7->5->1
