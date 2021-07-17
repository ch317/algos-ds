from Node import Node, breadthFirstSearch1, depthFirstSearch1

def createBinaryTree(array, child): #is Search binary tree?

    if len(array) == 1:
        return Node(array[0])

    if len(array) == 2:
        if child == "left":
            node1 = Node(array[1])
            node2 = Node(array[0])
            node1.addChild(node2)
            return node1
        else:
            node1 = Node(array[0])
            node2 = Node(array[1])
            node1.addChild(node2)
            return node1

    middleIdx = int(len(array) / 2)
    leftChild = createBinaryTree(array[:middleIdx], "left")
    rightChild = createBinaryTree(array[middleIdx+1:], "right")

    node = Node(array[middleIdx])
    node.addChild(leftChild)
    node.addChild(rightChild)

    return node


array = [1, 2, 3, 4, 5]
treeRoot = createBinaryTree(array, "left")
breadthFirstSearch1(treeRoot) #BFS: 3, 2, 4, 1, 5
depthFirstSearch1(treeRoot) #DFS: 3, 2, 1, 4, 5

array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
treeRoot = createBinaryTree(array, "left")
breadthFirstSearch1(treeRoot) #BFS: 5, 3, 8, 2, 4, 7, 9, 1, 6
depthFirstSearch1(treeRoot) #DFS: 5, 3, 2, 1, 4, 8, 7, 6, 9