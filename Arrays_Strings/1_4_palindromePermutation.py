# Given a string, write a function to check if it is a permutation of a palindrome

def getIntOfChar(c):
    return ord(c) - ord('a')

# Assuming we don't care about case sensitive nor spaces

#O(n) time O(1) space [since we create a char_set with 128 elements]
def isPalindromePermutation(s):
    char_set_count = [0 for i in range(128)]
    s = s.lower().replace(" ", "")
    for char in s:
        i = getIntOfChar(char)
        char_set_count[i] = char_set_count[i] + 1
    
    count_lettersWithOddCount = 0
    for letter_count in char_set_count:
        if letter_count%2 != 0:
            count_lettersWithOddCount += 1
            if count_lettersWithOddCount > 1: #at least 2 letters with odd count => cant form a palindrome
                return False
    
    return True

#Tests
print(isPalindromePermutation("Tact Coa")) #True
print(isPalindromePermutation("aaccaa")) #True
print(isPalindromePermutation("aaccaad")) #True
print(isPalindromePermutation("a")) #True
print(isPalindromePermutation("aa")) #True
print(isPalindromePermutation("ab")) #False
print(isPalindromePermutation("aaccfaad")) #False

