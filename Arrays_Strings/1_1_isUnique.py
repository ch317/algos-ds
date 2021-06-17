#Implement an algorithm to determine if a string has all unique characters. What if you 
#cannot use additional data structures?

# O(n) computation, O(n) space 
def isUnique1(s):
    letters = {}
    for char in s:
        if char in letters:
            return False
        letters[char] = True

    return True

print("isUnique1()")
print(isUnique1("aiehba")) #False
print(isUnique1("abcdefghijk")) #True
print(isUnique1("aa")) #False
print(isUnique1("a")) #True

#Without using Dict data structure, only algorithm
#O(n^2) computation brute force
def isUnique2(s):
    n = len(s)
    for i in range(n):
        for j in range(i+1,n):
            if s[i] == s[j]:
                return False
    
    return True

print("\nisUnique2()")
print(isUnique2("aiehba")) #False
print(isUnique2("abcdefghijk")) #True
print(isUnique2("aa")) #False
print(isUnique2("a")) #True

#returns int number of char ('a' returns 0, 'b' returns 1...) 
def getIntOfChar(c):
    return ord(c) - ord('a')

#O(n) computation O(1) space creating a bool array of length 128 where a[i] is True
# if i-character appears
def isUnique3(s):
    char_set = [False for i in range(128)]

    for char in s:
        i = getIntOfChar(char) 
        if char_set[i]:
            return False

        char_set[i] = True

    return True

print("\nisUnique3()")
print(isUnique2("aiehba")) #False
print(isUnique2("abcdefghijk")) #True
print(isUnique2("aa")) #False
print(isUnique2("a")) #True