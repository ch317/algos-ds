from Node import Node, breadthFirstSearch1

def validateSubtreeBST(node):
    if len(node.children) == 0:
        return (node.data, True)
    
    if len(node.children) == 1:
        leftChild = validateSubtreeBST(node.children[0])
        if leftChild[1] is False:
            return (node.data, False)

        if node.data > leftChild[0]:
            return (node.data, True)
        
        return (node.data, False)

    
    leftChild = validateSubtreeBST(node.children[0])
    rightChild = validateSubtreeBST(node.children[1])

    if leftChild[1] is False or rightChild[1] is False:
        return (node.data, False)

    if node.data > leftChild[0] and node.data < rightChild[0]:
        return (node.data, True)
    
    return (node.data, False)


def validateBST(root):
    return validateSubtreeBST(root)[1]


def createNonBST():
    root = Node(5)
    node1_1 = Node(3)
    node1_2 = Node(4)
    root.addChild(node1_1)
    root.addChild(node1_2)

    node2_1 = Node(1)
    node1_1.addChild(node2_1)

    node3_1 = Node(0)
    node3_2 = Node(2)

    node2_1.addChild(node3_1)
    node2_1.addChild(node3_2)

    return root

def createBST():
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

#Test
root = createNonBST()
breadthFirstSearch1(root) #Print tree following BFS order
print(validateBST(root)) #Print False

root = createBST()
breadthFirstSearch1(root) #Print tree following BFS order
print(validateBST(root)) #Print True