
def getCoordenatesAfter90DegRotation(n, coordinates):
    rowRotCoordinates = coordinates[1] #row coordinate of rotated matrix is the column coordinate
    colRotCoordinates = n - 1 - coordinates[0] #column coordinate of rotated matrix is the inverse of row coordinate
    return (rowRotCoordinates, colRotCoordinates)


def rotateMatrix(M):
    nRows = len(M)
    nColumns = nRows #since it is NxN matrix

    Mrot= [([0]*nColumns) for i in range(nRows)] #Initialize mRotated with all zeros

    for i in range(nRows):
        for j in range(nColumns):
            coordenatesRot = getCoordenatesAfter90DegRotation(nRows, (i,j))
            Mrot[coordenatesRot[0]][coordenatesRot[1]] = M[i][j]

    return Mrot

M1 = [["a","b","c"], ["d","e","f"], ["g","h","i"]]
M1rot = rotateMatrix(M1)
print(M1rot) # [["g","d","a"], ["h","e","b"], ["i","f","c"]]