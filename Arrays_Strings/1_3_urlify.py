#Write a method to replace all spaces in a string with '%20'. You may assume that the string 
#has sufficient space at the end to hold the additional characters, and that you are given the "true" 
#length of the string

#Replace every space with %20
def urlify1(s):
    finalUrl = ""

    for char in s:
        if char == " ":
            finalUrl = finalUrl + "%20"
        else:
            finalUrl = finalUrl + char

    return finalUrl

print(urlify1("Testing url program"))
print(urlify1("  two spaces at the beginning and two at the end  "))
print(urlify1("     "))


# New invented exercise:  
# Write a method to replace the first space char found in a string with '%20'.
# If there are many consecutive spaces, just put one %20 instead of multiple

#O(n) assuming char concatenating at the end is O(1)
#O(n^2) assuming char concatenating makes a copy of current string in O(n)
def urlify2(s):
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

print(urlify2("Testing url program"))
print(urlify2("  two spaces at the beginning and two at the end  "))
print(urlify2("     "))

