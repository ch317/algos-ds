#Write a method to replace all spaces in a string with '%20'. You may assume that the string 
#has sufficient space at the end to hold the additional characters, and that you are given the "true" 
#length of the string

#O(n) assuming char concatenating at the end is O(1)
#O(n^2) assuming char concatenating makes a copy of current string in O(n)
def urlify(s):
    finalUrl = ""
    lastCharIsNotSpace = True

    for char in s:
        if char != " ":
            finalUrl = finalUrl + char
            lastCharIsNotSpace = True
        else:
            if lastCharIsNotSpace:
                finalUrl = finalUrl + "%20"
                lastCharIsNotSpace = False
    
    return finalUrl

print(urlify("Testing url program"))
print(urlify("  two spaces at the beginning and two at the end  "))
print(urlify("     "))

