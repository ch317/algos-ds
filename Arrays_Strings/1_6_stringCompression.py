# Implement a method to perform basic string compression using the counts 
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the 
# "compressed" string would not become smaller than the original string, your method should return 
# the original string

#O(n) if appending characters+count to sCompressed is O(1)
#O(n^2) if appending characters+count to sCompressed is O(n)
def compress(s):

    lastChar = s[0]
    countLastChar = 1
    sCompressed = ""
    needsCompression = False

    for i in range(1, len(s)):
        if s[i] == lastChar:
            needsCompression = True
            countLastChar += 1
        else:
            sCompressed = sCompressed + lastChar + str(countLastChar)
            lastChar = s[i]
            countLastChar = 1
    
    #Last element
    sCompressed = sCompressed + lastChar + str(countLastChar)

    if needsCompression:
        return sCompressed
    
    return s

print(compress("aabcccccaaa")) #a2b1c5a3
print(compress("abcdefggg")) #a1b1c1d1e1f1g3
print(compress("abcdef")) #abcdef (doesnt need compression)