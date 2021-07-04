from Stack import Stack, Node

## Class that implements a queue using two stacks.
## This second implementation uses an extra Boolean variable to optimize multiple adds or multiple removes
## Stack2 will be used as temporal stack for multiple peek() and remove() functions in a row. 
## Stack1 will be used as the base stack storage in the normal order
class MyQueue1:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
        self.lastCallWasAdd = True
    
    def add(self, node):
        if self.lastCallWasAdd: #We use stack1 which is in normal order
            self.stack1.push(node)
        else: #data is in Stack2 in reversed order so we have to restore the original in stack1 and push as before
            while not self.stack2.isEmpty(): #We reverse the operation and set Stack1 identical as before but without the last element of the stack
                node = self.stack2.pop()
                self.stack1.push(Node(node.data))
            self.stack1.push(node)
            self.lastCallWasAdd = True
    
    def remove(self):
        if not self.lastCallWasAdd: #last call was peek() or remove()
            if self.stack2.isEmpty():
                raise IndexError
            self.stack2.pop()
        else:
            if self.stack1.isEmpty():
                raise IndexError
            while not self.stack1.isEmpty():
                node = self.stack1.pop()
                self.stack2.push(Node(node.data))
            
            self.stack2.pop()
            self.lastCallWasAdd = False
    
    def peek(self):
        if not self.lastCallWasAdd: #last call was peek() or remove()
            if self.stack2.isEmpty():
                raise IndexError
            return self.stack2.peek()
        else:
            if self.stack1.isEmpty():
                raise IndexError
            while not self.stack1.isEmpty():
                node = self.stack1.pop()
                self.stack2.push(Node(node.data))
            
            self.lastCallWasAdd = False
            return self.stack2.peek()
    
    def isEmpty(self):
        if self.lastCallWasAdd:
            return self.stack1.isEmpty()
        else:
            return self.stack2.isEmpty()

    def print(self):
        if self.lastCallWasAdd:
            if self.stack1.isEmpty():
                print("Queue is empty")
                return

            current = self.stack1.top
            queueStr = ""
            firstIter = True
            while current != None:
                if firstIter:
                    queueStr += str(current.data)
                    firstIter = False
                else:
                    queueStr += "->" + str(current.data)
            
                current = current.next
            
            print(queueStr)
        
        else:
            if self.stack2.isEmpty():
                print("Queue is empty")
                return

            current = self.stack2.top
            queueStr = ""
            firstIter = True
            while current != None:
                if firstIter:
                    queueStr = str(current.data) + queueStr
                    firstIter = False
                else:
                    queueStr = str(current.data) + "->" + queueStr
            
                current = current.next
            
            print(queueStr)


# stuff to run always here such as class/def
def testMyQueue2():
    #Tests
    #1. We create an empty Queue:
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    #We create the Queue: 3->2->1 (first element of the queue is 1)
    queue1 = MyQueue1()
    queue1.add(node1)
    queue1.add(node2)
    queue1.add(node3)
    queue1.print() #3->2->1

    print(queue1.peek()) #Print 1
    queue1.remove() #We delete 1
    print(queue1.peek()) #Print 2
    queue1.print() #Print Top: 3->2
    print(queue1.isEmpty()) #Print False
    queue1.remove()
    queue1.remove()
    print(queue1.isEmpty()) #Print True
    queue1.print() #Empty queue
    queue1.add(Node(4))
    queue1.add(Node(5))
    queue1.print() #5->4

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
    testMyQueue2()