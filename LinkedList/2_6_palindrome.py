from LinkedList import LinkedList, Node

def isPalindrome(list):
    i=0
    j=len(list)-1

    while (i < j):
        if list[i] != list[j]:
            return False
        
        i += 1
        j -= 1

    return True

def isLinkedListPalindrome(linkedList):

    list1 = []
    current = linkedList.head

    #1. We traverse the linked list and add the node value to a python list
    while (current != None):
        list1.append(current.data)
        current = current.next
    
    return isPalindrome(list1)

def test():
    list1 = LinkedList() # a->b->c->c->b->a
    list1.add(Node("a"))
    list1.add(Node("b"))
    list1.add(Node("c"))
    list1.add(Node("c"))
    list1.add(Node("b"))
    list1.add(Node("a"))
    print(isLinkedListPalindrome(list1)) #True

    list1 = LinkedList() #a->b->c->d->e->f
    list1.add(Node("a"))
    list1.add(Node("b"))
    list1.add(Node("c"))
    list1.add(Node("d"))
    list1.add(Node("e"))
    list1.add(Node("f"))
    print(isLinkedListPalindrome(list1)) #False

test()
