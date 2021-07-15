from NodeGraph import Node, createSampleGraph
import queue


#We will make a BFS starting from node1 to check if we find node2. If found, return True. Otherwise, return False.
def isDirectPath(node1, node2):
    q1 = queue.Queue()
    q1.put(node1)

    while q1.qsize() != 0:
        current = q1.get()
        current.visited = True
        if current == node2: #we've found node2 starting from node1 => there is a direct path node1->node2
            return True

        for children in current.children:
            if not children.visited:
                q1.put(children)
                children.visited = True
    
    #We've finished the BFS and we have not reached node2 from node1, therefore there is no direct path node1->node2
    return False

# Sample Graph is the following:
#  1 ➡️  3
# ⬇️   ↙️
#  4  ↙️
# ⬇️↙️
#  2 ➡️ 5
#Testing
def test1():
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

    print(isDirectPath(node1, node2)) #True: node1->node4->node2 or node1->node3->node2

def test2():
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

    print(isDirectPath(node3, node5)) #True: node3->node2->node5

def test3():
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

    print(isDirectPath(node3, node1)) #False: Can't reach node1 from node3

def test4():
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

    print(isDirectPath(node5, node2)) #False: Can't reach node2 from node5

test1() #True
test2() #True
test3() #False
test4() #False
