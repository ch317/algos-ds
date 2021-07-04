from Stack import Stack, Node

class StackOfStacks:

    def __init__(self, threshold):
        self.stackOfStacks = Stack()
        self.numElements = 0
        self.Threshold = threshold
    
    def push(self, node):
        if self.numElements % self.Threshold == 0:
            self.stackOfStacks.push(Node(Stack()))
        self.stackOfStacks.peek().push(node)
        self.numElements += 1

    def pop(self):
        if self.numElements == 0: #Only edge case since if numElements != 0, there will always be at least 1 stack with 1 element
            raise IndexError

        self.stackOfStacks.peek().pop()

        if self.numElements % self.Threshold == 1: #Last stack only has one element: 1. we pop that element (previous lane) 2. we pop the top stack in stackOfStacks
            self.stackOfStacks.pop()
        
        self.numElements -= 1
    
    def print(self):
        if self.numElements == 0:
            print("Stack of stacks is empty")
            return
        
        currentNode = self.stackOfStacks.top

        while currentNode != None:
            currentNode.data.print() #currentNode.data are each one of the substacks contained in the stackOfStacks stack
            currentNode = currentNode.next
    
# stuff to run always here such as class/def
def testStackOfStacks():
    #Tests
    #1. We create an empty Stack:
    node1 = Node(3)
    node2 = Node(2)
    node3 = Node(6)
    node4 = Node(1)
    node5 = Node(5)

    node6 = Node(1)

    #Lets use Threshold = 5, and we will add 6 elements to the stackOfStacks (first stack full and second with 1 element)
    stackOfStacks = StackOfStacks(threshold=5)
    stackOfStacks.push(node1)
    stackOfStacks.push(node2)
    stackOfStacks.push(node3)
    stackOfStacks.push(node4)
    stackOfStacks.push(node5)
    stackOfStacks.push(node6)
    stackOfStacks.print()

    stackOfStacks.pop() #Now we only have 1 stack with 5 elements
    stackOfStacks.print()

    stackOfStacks.pop() #1 stack with 4 elements
    stackOfStacks.print()

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   testStackOfStacks()