#Given two strings, write a method to decide if one is a permutation of the 
#other

def getDictLettersCountFromStr(s):
    lettersCount = {}

    for char in s:
        if char in lettersCount:
            lettersCount[char] = lettersCount[char] + 1
        else:
            lettersCount[char] = 0
    
    return lettersCount

def arePermutationsFromDict(dict1, dict2):
    for key, value in dict1.items():
        if key not in dict2: #Letter in dict1 and not in dict2 means permutation is impossible
            return False

        if value != dict2[key]: #Letter is in dict1 and dict2 but not the same number of times => permutation is impossible.
            return False

    return True #Every letter in dict1 is in dict2 and they appear the same number of times => it's a permutation

#O(n1 + n2) computation
#O(n1 + n2) storage
def checkPermutation(s1, s2):

    if len(s1) != len(s2):
        return False

    s1LettersCount = {}
    s2LettersCount = {}

    s1LettersCount = getDictLettersCountFromStr(s1)
    s2LettersCount = getDictLettersCountFromStr(s2)

    return arePermutationsFromDict(s1LettersCount, s2LettersCount)


s1 = "HEYIMTE"
s2 = "EEHITMY"
print(checkPermutation(s1, s2)) #True

s1 = "HELLO"
s2 = "BYE"
print(checkPermutation(s1, s2)) #False

s1 = "test1"
s2 = "test2"
print(checkPermutation(s1, s2)) #False

s1 = "abcdefghi"
s2 = "ihgfedcba"
print(checkPermutation(s1, s2)) #True