from LinkedList import LinkedList, Node
import math

#Returns a list with the digits of the number n
def getDigits(n):
    #1 we calculate the number of digits of n
    digitsCount = int(math.log10(n)) + 1
    digits = [0 for i in range(digitsCount)] #Initialize digits to 0

    for i in range(digitsCount):
        digits[digitsCount-1-i] = int(n/10**i)%10
    
    return digits

def sumList(node, n):

    if node is None:
        return 0

    sumAtThisNode = node.data*10**n + sumList(node.next, n+1)
    return sumAtThisNode

def sumLists(list1, list2):

    sumList1 = sumList(list1.head, 0)
    sumList2 = sumList(list2.head, 0)
    
    sum = sumList1 + sumList2
    digits = getDigits(sum)
    finalList = LinkedList()
    for digit in reversed(digits):
        node = Node(digit)
        finalList.add(node)
    #get each number of sum one by one and create a list in the correct order

    return finalList

def test():
    list1 = LinkedList() #7->1->6 (represents 617)
    list1.add(Node(7))
    list1.add(Node(1))
    list1.add(Node(6))
    list2 = LinkedList() #5->9->2 (represents 295)
    list2.add(Node(5))
    list2.add(Node(9))
    list2.add(Node(2))
    sumList = sumLists(list1, list2)
    sumList.printList() #2->1->9 (represents 912)

test()

#Function creating the sumList directly. Assuming both lists have the same length!
def sumListsEqualLength(list1, list2):

    p1 = list1.head
    p2 = list2.head
    carry = 0
    sumList = LinkedList()

    while p1 != None:
        sum = p1.data + p2.data + carry
        unit = sum%10
        if sum >= 10:
            carry = 1
        else:
            carry = 0

        sumList.add(Node(unit))
        p1 = p1.next
        p2 = p2.next
    
    #Last element only if carry is 1
    if carry == 1:
        sumList.add(Node(1))
    
    return sumList

def testEqualLength():
    list1 = LinkedList() #7->1->6 (represents 617)
    list1.add(Node(7))
    list1.add(Node(1))
    list1.add(Node(6))
    list2 = LinkedList() #5->9->2 (represents 295)
    list2.add(Node(5))
    list2.add(Node(9))
    list2.add(Node(2))
    sumList = sumLists(list1, list2)
    sumList.printList() #2->1->9 (represents 912)

    list1 = LinkedList() #9->9->8 (represents 899)
    list1.add(Node(9))
    list1.add(Node(9))
    list1.add(Node(8))
    list2 = LinkedList() #7->7->7 (represents 777)
    list2.add(Node(7))
    list2.add(Node(7))
    list2.add(Node(7))
    sumList = sumLists(list1, list2)
    sumList.printList() #6->7->6->1 (represents 1676)

testEqualLength()