# Assume you have a method isSubstring which checks if one word is a substring 
# of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one 
# call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat")

#We assume we have isSubstring and we can only call it once
def isSubstring(s1, s2):
    return s2 in s1

#Since we can only call once to isSubstring, we concatenate s2 with itself
#If s1 is substring of this concatenation, then s2 is a rotation of s1
def stringRotation(s1, s2):
    if (len(s1) != len(s2)):
        return False

    s2Concatenated = s2 + s2
    return s1 in s2Concatenated


# Tests
s1 = "waterbottle"
s2 = "erbottlewat"
print(stringRotation(s1,s2)) #True

s1 = "waterbottle"
s2 = "bottleretaw"
print(stringRotation(s1,s2)) #False

