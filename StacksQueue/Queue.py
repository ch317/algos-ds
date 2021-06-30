class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, node):
        #If list was empty, then we set first and last to this new node added
        if self.first == None:
            self.first = node
            self.last = node
            return

        node.next = self.last
        self.last = node

    def remove(self):
        if self.first is None: #Queue is empty
            raise TypeError
        
        if self.first == self.last: #Queue has 1 element
            self.first = None
            self.last = None
            return
        
        #If Queue has >=2 elements, we traverse the queue starting from last until we find second to element and update
        current = self.last
        while current.next != self.first:
            current = current.next
        
        #Here current points to the second element of the Queue
        current.next = None
        self.first = current     
    
    def peek(self):
        if self.first is None:
            raise TypeError

        return self.first.data

    def isEmpty(self):
        return self.first is None
    
    #Last element of the queue is on the left and first element is on the right "a->b->c"
    def print(self):
        if self.first is None:
            print("Empty Queue")
            return
        
        current = self.last
        queueStr = ""
        while current.next != None:
            queueStr += str(current.data) + "->"
            current = current.next
        
        queueStr += str(current.data)
        
        print(queueStr)

# stuff to run always here such as class/def
def testQueue():
    #Tests
    #1. We create an empty Queue:
    node1 = Node(5)
    node2 = Node(3)
    node3 = Node(2)

    #We create the Queue Top: 2->3->5
    queue = Queue()
    queue.add(node1)
    queue.add(node2)
    queue.add(node3)
    queue.print() #2->3->5

    print(queue.peek()) #Print 5
    queue.remove() #We delete 5
    print(queue.peek()) #Print 3
    queue.print() #Print Top: 2->3
    print(queue.isEmpty()) #Print False
    queue.remove()
    queue.remove()
    print(queue.isEmpty()) #Print True
    queue.print() #Empty queue

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
    testQueue()