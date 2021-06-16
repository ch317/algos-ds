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
