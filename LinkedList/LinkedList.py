class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None

    def add(self, node):
        #Exceptional case when we add the first element in the LinkedList
        if self.head == None:
            self.head = node
            return

        current = self.head
        while(current.next != None):
            current = current.next
        
        current.next = node


    #Removes node with value <value> from the LinkedList if it exists.
    def remove(self, data):
        current = self.head

        if current == None: #LinkedList is empty
            return

        if current.data == data: #value is in the head of linke list -> need removal
            self.head = current.next
            return

        while current.next != None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def printList(self):
        if self.head == None:
            print("Empty list")
            return

        current = self.head
        strList = ""
        while(current.next != None):
            strList += str(current.data) + "->"
            current = current.next

        strList += str(current.data)
        print(strList)

# stuff to run always here such as class/def
def main():
    #Tests
    #1. We create an empty linked list:
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    linkedList = LinkedList()
    linkedList.add(node1)
    linkedList.add(node2)
    linkedList.add(node3)
    linkedList.printList() #print 1 2 3
    print("----------")
    linkedList.remove(2)
    linkedList.printList() #print 1 3
    print("----------")
    linkedList.remove(1)
    linkedList.printList() #print 3
    print("----------")
    linkedList.remove(3)
    linkedList.printList() #print nothing

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   main()