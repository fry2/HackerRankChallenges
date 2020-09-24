import math


def encryption(s):
    sClean = [i for i in s if not(i == ' ')]
    bnds = [math.floor(math.sqrt(len(sClean))), math.ceil(math.sqrt(len(sClean)))]
    if not(bnds[0]*bnds[1] >= len(sClean)):
        maxVal = max(bnds)
        bnds = [maxVal, maxVal]
        #raise Exception('rows times cols not greater than L')
    outMat = [None] * bnds[1]
    for rCount in range(bnds[1]):
        enWord = list()
        for ii in range(rCount, len(sClean), bnds[1]):
            enWord.append(sClean[ii])
        outMat[rCount] = ''.join(enWord)
    print(' '.join(outMat))

# HackerRank practice challenge : https://www.hackerrank.com/challenges/encryption/problem

encryption('haveaniceday')