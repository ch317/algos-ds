class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    
    def __init__(self):
        self.top = None
    
    def push(self, node):    

        node.next = self.top
        self.top = node

    def peek(self):
        if self.top is None:
            raise TypeError

        return self.top.data
    
    def pop(self):
        if self.top is None:
            raise TypeError
        
        nodeToPop = self.top
        self.top = self.top.next
        return nodeToPop
        
    def isEmpty(self):
        return self.top is None
    
    #This method will traverse the stack as it is a linkedlist to print the elements.
    #The top of the stack will be the first element
    def print(self):
        if self.top is None:
            print("Empty stack")
            return

        current = self.top
        stackStr = "Top: "
        while current.next != None:
            stackStr += str(current.data) + "--"
            current = current.next

        stackStr += str(current.data)
        print(stackStr)


# stuff to run always here such as class/def
def testStack():
    #Tests
    #1. We create an empty Stack:
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    #We create the stack Top: 3--2--1
    stack = Stack()
    stack.push(node1)
    stack.push(node2)
    stack.push(node3)
    stack.print()

    print(stack.peek()) #Print 3
    pop = stack.pop() #We delete 3
    print(stack.peek()) #Print 2
    stack.print() #Print Top: 2--1
    print(stack.isEmpty()) #Print False
    pop = stack.pop()
    pop = stack.pop()
    print(stack.isEmpty()) #Print True
    stack.print() #Empty stack

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   testStack()