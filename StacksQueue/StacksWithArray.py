#Implementation of 3 stacks with 1 array

n = 100 #Parameter to adjust for the length of the array
stacks = [0 for i in range(n)]

#offset = max length of each substack
offset = int(n/3) - 1
s1Start = 0
s1End = offset
s2Start = s1End + 1
s2End = s2Start + offset
s3Start = s2End + 1
s3End = s3Start + offset

#At first empty stacks, top of every stack is the start
top1Idx = -1
top2Idx = s2Start-1
top3Idx = s3Start-1

#Stack number only accepts a number in [1,2,3]
#value must be an integer
def push(stackNumber, value):
    if stackNumber not in [1, 2, 3]:
        raise ValueError

    if not isinstance(value, int):
        raise TypeError
    
    if stackNumber == 1:
        global top1Idx
        if top1Idx < s1End:
            top1Idx += 1
            stacks[top1Idx] = value
        else:
            raise IndexError

    elif stackNumber == 2:
        global top2Idx
        if top2Idx < s2End:
            top2Idx += 1
            stacks[top2Idx] = value
        else:
            raise IndexError
    
    elif stackNumber == 3:
        global top3Idx
        if top3Idx < s3End:
            top3Idx += 1
            stacks[top3Idx] = value
        else:
            raise IndexError

#Pops the last number in the stack
def pop(stackNumber):
    if stackNumber not in [1, 2, 3]:
        raise ValueError
    
    if stackNumber == 1:
        global top1Idx
        if top1Idx < 0: #Empty stack
            raise IndexError

        tmp = stacks[top1Idx]
        stacks[top1Idx] = 0
        top1Idx -= 1

    elif stackNumber == 2:
        global top2Idx
        if top2Idx < s2Start: #Empty stack
            raise IndexError

        tmp = stacks[top2Idx]
        stacks[top2Idx] = 0
        top2Idx -= 1
    
    elif stackNumber == 3:
        global top3Idx
        if top3Idx < s3Start: #Empty stack
            raise IndexError

        tmp = stacks[top3Idx]
        stacks[top3Idx] = 0
        top3Idx -= 1

print("Empty stacks: ")
print(stacks)

#We push to stack1 3 different values: 3, 7, 11
push(1, 3)
push(1, 7)
push(1, 11)
print(stacks)
print(top1Idx) #top1Idx must be 2 (index of top of stack1)
print(stacks[top1Idx]) #element at the top of stack 1 is 11

push(2, 4)
push(2, 5)
push(2, 6)
print(top2Idx)
print(stacks[top2Idx])
print(stacks)

push(3, 999)
print(top3Idx)
print(stacks[top3Idx])
print(stacks)

#Testing exceptions
#push(4, 10) #Value Error
#push(2, 2.5) #Type Error
pop(1)
pop(2)
pop(3)
pop(3) #Should give index error since stack 3 is empty now
print(stacks)