import queue

class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
    
    def __str__(self):
        return self.data
    
    def addChild(self, node):
        self.children.append(node)
    
####  8
### 4 6 10
## 2 1    20
def createSampleTree():
    root = Node(8)
    node11 = Node(4)
    node12 = Node(6)
    node13 = Node(10)
    node21 = Node(2)
    node22 = Node(1)
    node26 = Node(20)

    root.addChild(node11)
    root.addChild(node12)
    root.addChild(node13)

    node11.addChild(node21)
    node11.addChild(node22)

    node13.addChild(node26)

    return root

def depthFirstSearch(node):
    print(node.data)
    if len(node.children) == 0:
        return
    
    for children in node.children:
        depthFirstSearch(children)

def depthFirstSearch1(root):
    print("Depth first search:")
    stack1 = [] #we will use lists as stack since python provides O(1) method for push and pop
    stack1.append(root)
    while len(stack1) != 0:
        current = stack1.pop()
        print(current.data)
        for child in reversed(current.children):
            stack1.append(child)

def breadthFirstSearch1(root):
    print("Breadth first search:")
    root = createSampleTree()
    q1 = queue.Queue()
    q1.put(root)
    while q1.qsize() != 0:
        current = q1.get()
        print(current.data)
        for child in current.children:
            q1.put(child)

if __name__ == "__main__":
    # stuff only to run when not called via 'import' here
    root = createSampleTree()
    depthFirstSearch1(root)

    root = createSampleTree()
    breadthFirstSearch1(root)

    #Depth first search recursive
    print("Depth first search (recursive implementation):")
    root = createSampleTree()
    depthFirstSearch(root)
