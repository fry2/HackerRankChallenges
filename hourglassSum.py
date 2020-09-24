def hourglassSum(arr):
    outArr = list()
    maxVal = -1000
    for row in range(1,5):
        for col in range(1,5):
            curVal = arr[row][col]+arr[row-1][col]+arr[row+1][col]+arr[row-1][col-1]+arr[row-1][col+1] \
                     + arr[row+1][col-1] + arr[row+1][col+1]
            if curVal > maxVal:
                maxVal = curVal
    print(maxVal)
    return maxVal

# HackerRank practice challenge : https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

arr =  [[1,1,1,0,0,0],
        [0,1,0,0,0,0],
        [1,1,1,0,0,0],
        [0,0,2,4,4,0],
        [0,0,0,2,0,0],
        [0,0,1,2,4,0]]
hourglassSum(arr)