from Node import Node, breadthFirstSearch1, depthFirstSearch1

#list1 is a list of lists
#list2 is a list of lists
#This function returns a single list of lists by combining both lists of lists with the same index.
#This single list of lists returned by this function represents the nodes at the same depth
def combineListsSameDepth(list1, list2):

    listLong = list1
    listShort = list2

    if len(list1) < len(list2):
        listLong = list2
        listShort = list1

    for i in range(len(listShort)):
        subListShort = listShort[i]
        for node in subListShort:
            listLong[i].append(node)
    
    return listLong

def listOfDepths(node):

    if len(node.children) == 0:
        return [[node]]

    if len(node.children) == 1:
        leftList = listOfDepths(node.children[0])
        leftList.insert(0, [node])
        return leftList
    
    leftList = listOfDepths(node.children[0])
    rightList = listOfDepths(node.children[1])
    listFinal = combineListsSameDepth(leftList, rightList)
    listFinal.insert(0, [node])
    return listFinal


root = Node(5)

node1_1 = Node(3)
node1_2 = Node(8)
root.addChild(node1_1)
root.addChild(node1_2)

node2_1 = Node(1)
node2_2 = Node(4)
node1_1.addChild(node2_1)
node1_1.addChild(node2_2)

node2_3 = Node(6)
node2_4 = Node(9)
node1_2.addChild(node2_3)
node1_2.addChild(node2_4)

node3_1 = Node(0)
node3_2 = Node(2)
node3_3 = Node(7)

node2_1.addChild(node3_1)
node2_1.addChild(node3_2)
node2_3.addChild(node3_3)

list = listOfDepths(root)
countList = 1
print(list)
for l in list: #[[5], [3, 8], [1, 4, 6, 9], [0, 2, 7]]
    print("List " + str(countList))
    countList += 1
    for node in l:
        print(node)

root = Node(5)

node1_1 = Node(3)
root.addChild(node1_1)
node2_1 = Node(1)
node2_2 = Node(4)
node1_1.addChild(node2_1)
node1_1.addChild(node2_2)
node3_1 = Node(0)
node3_2 = Node(2)
node2_1.addChild(node3_1)
node2_1.addChild(node3_2)
list = listOfDepths(root)
countList = 1
print(list)
for l in list: #[[5], [3], [1, 4], [0, 2]]
    print("List " + str(countList))
    countList += 1
    for node in l:
        print(node)