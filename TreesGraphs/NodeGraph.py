import queue

class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.visited = False
    
    def __str__(self):
        return str(self.data)
    
    def addChild(self, node):
        self.children.append(node)

#  1 ➡️  3
# ⬇️   ↙️
#  4  ↙️
# ⬇️↙️
#  2 ➡️ 5

def createSampleGraph():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    node1.addChild(node3)
    node1.addChild(node4)

    node2.addChild(node5)

    node3.addChild(node2)

    node4.addChild(node2)

    return node1

def depthFirstSearch(node):
    print(node.data)
    node.visited = True
    for child in reversed(node.children):
        if child.visited is False:
            depthFirstSearch(child)

def breadthFirstSearch(node):
    q1 = queue.Queue()
    q1.put(node)
    while q1.qsize() != 0:
        current = q1.get()
        print(current.data)
        current.visited = True
        for child in current.children:
            if child.visited is False:
                q1.put(child)
                child.visited = True


    

if __name__ == "__main__":
    # stuff only to run when not called via 'import' here
    node1 = createSampleGraph()
    print("Breadth first search:")
    depthFirstSearch(node1) #1->4->2->5->3

    print("\nDepth first search:")
    node1 = createSampleGraph()
    breadthFirstSearch(node1)

