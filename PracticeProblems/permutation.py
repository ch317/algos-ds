def permutation(strInput):
    if len(strInput) == 0:
        return [""]
    elif len(strInput) == 1:
        return [strInput]
    
    prefix = strInput[0]
    permutationsWithoutPrefix = permutation(strInput[1:])

    listPermutations = []
    for permutationWithoutPrefix in permutationsWithoutPrefix:
        for i in range(len(permutationWithoutPrefix) + 1):
            copyPermutation = permutationWithoutPrefix[:]
            newPermutation =  copyPermutation[:i] + prefix + copyPermutation[i:]
            listPermutations.append(newPermutation)
    
    return listPermutations

permutations = permutation("abcd")
print(permutations)
