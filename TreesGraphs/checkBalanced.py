from Node import Node, breadthFirstSearch1

def calculateSubtreeHeight(node):

    if len(node.children) == 0:
        return (1, True)

    leftSubtreeHeight = (0, True)
    rightSubtreeHeight = (0, True)

    if len(node.children) == 1:
        leftSubtreeHeight = calculateSubtreeHeight(node.children[0])
    else:
        leftSubtreeHeight = calculateSubtreeHeight(node.children[0])
        rightSubtreeHeight = calculateSubtreeHeight(node.children[1])

    if leftSubtreeHeight[1] is False or rightSubtreeHeight[1] is False: #If one node returns False as second argument, the whole tree is not balanced and we return False up to the first call
        return (-1, False)
    
    if abs(leftSubtreeHeight[0] - rightSubtreeHeight[0]) > 1:
        return (-1, False)
    
    return (1 + max(leftSubtreeHeight[0], rightSubtreeHeight[0]), True)

def checkBalanced(root):
    return  calculateSubtreeHeight(root)[1] #Second element of the tuple is True if the tree is balanced and False otherwise.

def createNotBalancedTreeSample():
    root = Node(5)
    node1_1 = Node(3)
    node1_2 = Node(8)
    root.addChild(node1_1)
    root.addChild(node1_2)

    node2_1 = Node(1)
    node1_1.addChild(node2_1)

    node3_1 = Node(0)
    node3_2 = Node(2)

    node2_1.addChild(node3_1)
    node2_1.addChild(node3_2)

    return root

def createBalancedTreeSample():
    root = Node(5)
    node1_1 = Node(3)
    node1_2 = Node(8)
    root.addChild(node1_1)
    root.addChild(node1_2)

    node2_1 = Node(1)
    node1_1.addChild(node2_1)

    node2_2 = Node(10)
    node1_2.addChild(node2_2)

    return root

#test
root = createNotBalancedTreeSample()
breadthFirstSearch1(root) #Print tree following BFS order
print(checkBalanced(root)) #Print False

root = createBalancedTreeSample()
breadthFirstSearch1(root) #Print tree following BFS order
print(checkBalanced(root)) #Print True
