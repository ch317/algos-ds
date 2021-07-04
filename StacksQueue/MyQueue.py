from Stack import Stack, Node

## Class that implements a queue using two stacks.
## This first implementation won't use optimizations for multiple adds or removes in a row.
## This means every remove will get the last element of Stack1 (first of the queue), we use Stack2
## for temporal storage and we traverse Stack2 to recover the original order of Stack1
## Removes are always O(N). Adds are always O(1) in MyQueue1
class MyQueue1:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
    
    def add(self, node):
        self.stack1.push(node)

    #Removes the first element of the Queue, it doesn't return anything
    def remove(self):
        #1. We use Stack2 as temporal storage and we include every element but the last of Stack1 
        # (which represents the first element of the queue which needs to be removed)
        if self.stack1.isEmpty():
            raise IndexError

        while not self.stack1.isEmpty():
            node = self.stack1.pop()
            self.stack2.push(Node(node.data))
        
        self.stack2.pop() #Pop the element of the temporal stack 2 (which is the elemend to be removed)

        while not self.stack2.isEmpty(): #We reverse the operation and set Stack1 identical as before but without the last element of the stack
            node = self.stack2.pop()
            self.stack1.push(Node(node.data))

    #Same implementation as before but returning the last node of Stack1 (which is the first node of the Queue)
    def peek(self):

        if self.stack1.isEmpty():
            raise IndexError
        
        while not self.stack1.isEmpty():
            node = self.stack1.pop()
            self.stack2.push(Node(node.data))
        
        dataFirstInQueue = self.stack2.peek() #Get the head of the temporal stack 2 (which is the elemend to be returned as the head of the queue)

        while not self.stack2.isEmpty(): #We reverse the operation and set Stack1 identical as before but without the last element of the stack
            node = self.stack2.pop()
            self.stack1.push(Node(node.data))

        return dataFirstInQueue

    def isEmpty(self):
        return self.stack1.isEmpty()
    
    #Hack implementation to use in the tests
    def print(self):
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

# stuff to run always here such as class/def
def testMyQueue1():
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

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
    testMyQueue1()

