def jumpingOnClouds(c):
    anchor = 0
    jumps = 0
    while anchor < len(c)-1:
        nextStep = c[anchor+1:anchor+3]
        if nextStep == [0, 1]:
            anchor += 1
        elif nextStep == [0, 0] or nextStep == [1, 0]:
            anchor += 2
        else:
            anchor += 1
        jumps += 1
    print(jumps)
    return jumps

# HackerRank practice challenge : https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

jumpingOnClouds([0,0,1,0,0,1,0])