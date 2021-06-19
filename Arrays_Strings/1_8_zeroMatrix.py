#MxN matrix

#Doing it in just one pass through the matrix, it is O(MxN*(M+N))

#O(MxN) if we store which rows and columns will need to be zeroes and iterate through the matrix again two more times.
def zeroMatrix(M):
    
    nRows = len(M)
    nColumns = len(M[0])

    rowsIdxToZero = [False for i in range(nRows)]
    columnsIdxToZero = [False for j in range(nColumns)]
    
    for i in range(nRows):
        for j in range(nColumns):
            if M[i][j] == 0:
                rowsIdxToZero[i] = True
                columnsIdxToZero[j] = True


    #Make rows 0
    for i in range(nRows):
        if rowsIdxToZero[i] is True:
            for j in range(nColumns):
                M[i][j] = 0
    
    #Make columns 0
    for j in range(nColumns):
        if columnsIdxToZero[j] is True:
            for i in range(nRows):
                M[i][j] = 0
    
    return M

M = [[1,0,2,4],[0,3,3,1],[2,2,4,0]]
print(zeroMatrix(M)) #Should be all 3x4 matrix all zeroes

M = [[1,0,2,4],[0,3,3,1],[2,2,4,7]] 
print(zeroMatrix(M)) #All zeros but M[2,3] and M[2,4]