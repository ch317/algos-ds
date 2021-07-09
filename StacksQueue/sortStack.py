from Stack import Stack, Node

def getMinElementAndStack(stack1):
    min = float("inf")
    minFound = False
    stack2 = Stack()
    #We traverse stack1 to obtain the min value, we use stack2 as temporal stack
    while not stack1.isEmpty():
        head1Node = stack1.pop()
        if head1Node.data < min:
            min = head1Node.data

        stack2.push(Node(head1Node.data))
    
    while not stack2.isEmpty():
        head2Node = stack2.pop()
        if head2Node.data == min and not minFound: #This only happens once and we don't add this element (first min Found) to the stack we want to return
            minFound = True
        else:
            stack1.push(Node(head2Node.data))
    
    return (min, stack1)

#Sorts a stack using only other stacks, returns the sorted stack
def sortStack(stack):
    sortedStackInverse = Stack()
    while not stack.isEmpty():
        (min, stack) = getMinElementAndStack(stack)
        sortedStackInverse.push(Node(min))
    
    sortedStack = Stack()
    while not sortedStackInverse.isEmpty():
        headStackInverseNode = sortedStackInverse.pop()
        sortedStack.push(Node(headStackInverseNode.data))
    
    return sortedStack

#Tests
stack1 = Stack()
stack1.push(Node(2))
stack1.push(Node(1))
stack1.push(Node(3))
stack1.push(Node(7))
stack1.push(Node(5))
stack1.push(Node(1))

sortedStack = sortStack(stack1)
sortedStack.print()