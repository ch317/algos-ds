def getIntOfChar(c):
    return ord(c) - ord('a')

def oneAway(s1, s2):
    #First filter: if difference in length is more than 1 return False
    if abs(len(s1) - len(s2)) > 1:
        return False

    sLong = s1
    sShort = s2
    if len(s2) > len(s1):
        sLong = s2
        sShort = s1

    #First option: Both strings have equal length, only difference by 1 char is available
    if len(sLong) == len(sShort):
        for i in range(len(sLong)):
            if sLong[i] != sShort[i]: #1 char difference, needs the rest to be equal, otherwise it is not one-way
                if sLong[i+1:] == sShort[i+1:]:
                    return True
                else:
                    return False
        
        return True
                
    #Second option: sLong is one character longer than sShort. If there is 1 character different, the rest must be the same so that a deletion
    #of 1 character means we can construct the second string.
    for i in range(len(sLong)):
        #Edge case: Last iteration and we haven't returned yet -> both strings are equal but in the last character (one insertion away)
        if i == len(sLong)-1:
            return True

        if sLong[i] != sShort[i]:
            if sLong[i+1:] == sShort[i:]:
                return True
            else:
                return False
    
    return True

#Test
print(oneAway("ples", "ale")) #False
print(oneAway("pale", "bake")) #False
print(oneAway("pale", "ple")) #True
print(oneAway("pale", "bale")) #True
print(oneAway("pales", "pale")) #True

#Implementeng logic in a more compact way
def oneAway2(s1, s2):
    #First filter: if difference in length is more than 1 return False
    if abs(len(s1) - len(s2)) > 1:
        return False

    sLong = s1
    sShort = s2
    if len(s2) > len(s1):
        sLong = s2
        sShort = s1
    
    for i in range(len(sLong)):
        if i == len(sLong)-1:
            return True

        if sLong[i] != sShort[i]: # 1st char difference
            if len(sLong) == len(sShort):
                return sLong[i+1:] == sShort[i+1:]
            else:
                return sLong[i+1:] == sShort[i:]

#Test2
print(oneAway2("ples", "ale")) #False
print(oneAway2("pale", "bake")) #False
print(oneAway2("pale", "ple")) #True
print(oneAway2("pale", "bale")) #True
print(oneAway2("pales", "pale")) #True