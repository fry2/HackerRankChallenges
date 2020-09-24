def surfaceArea(A):
    totalBlocks = 0
    links = 0
    numRows = 0
    for i in A:
        numRows += 1
        numCols = len(i)
        totalBlocks += sum(i)
    for row in range(numRows):
        for column in range(numCols):
            links += A[row][column]-1
            if not(column == numCols-1):
                links += min(A[row][column+1], A[row][column])
            if not(row == numRows-1):
                links += min(A[row+1][column], A[row][column])
    surface = 6*totalBlocks-2*links
    return surface

# HackerRank practice challenge : https://www.hackerrank.com/challenges/3d-surface-area/problem

area = surfaceArea([[1,3,4],[2,2,3],[1,2,4]])
print(area)