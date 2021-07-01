from Stack import Stack, Node

#StackMin gives the min value of the stack in O(1) time. For that, we will store an extra stack with the min values added to the original stack
class StackMin:
    
    def __init__(self):
        self.top = None
        self.minStack = Stack()
    
    def push(self, node):
        
        if self.minStack.isEmpty() or node.data <= self.minStack.peek():
            print("minStack is empty:" +str(self.minStack.isEmpty()))
            self.minStack.push(Node(node.data))
            print("minStack peek:" + str(self.minStack.peek()))

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
        if nodeToPop.data == self.minStack.peek():
            self.minStack.pop()

        self.top = self.top.next
        return nodeToPop
        
    def isEmpty(self):
        return self.top is None
    
    def min(self):
        return self.minStack.peek()
    
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
def testStackMin():
    #Tests
    #1. We create an empty Stack:
    node1 = Node(3)
    node2 = Node(2)
    node3 = Node(6)
    node4 = Node(1)
    node5 = Node(5)
    node6 = Node(1)

    stack = StackMin()
    stack.minStack.print()
    stack.push(node1)
    stack.push(node2)
    stack.push(node3)
    stack.push(node4)
    stack.push(node5)
    stack.push(node6)
    minStack = stack.minStack
    stack.print() #1--5--1--6--2--3
    minStack.print()

    print(stack.min()) #1
    stack.pop()
    stack.pop()
    stack.print() # 1--6--2--3
    print(stack.min()) #1
    stack.pop()
    stack.print() #6--2--3
    
    print(stack.min()) #2


if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   testStackMin()