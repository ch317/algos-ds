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
