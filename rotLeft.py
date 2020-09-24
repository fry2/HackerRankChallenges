def rotLeft(a, d):
    b = a[d:]+a[0:d]
    print(b)
    return b

# HackerRank practice challenge : https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

rotLeft([1,2,3,4,5],4)