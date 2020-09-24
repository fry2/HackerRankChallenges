import math


def nonDivisibleSubset(k, s):
    remainders = [i % k for i in s]
    cut = math.ceil(k/2)
    outNum = 0
    if remainders.count(0) > 0:
        outNum += 1
    if k % 2 == 0:
        if remainders.count(cut) > 0:
            outNum += 1
    for ii in range(1, cut):
        v1 = ii
        v2 = k-ii
        numv1 = remainders.count(v1)
        numv2 = remainders.count(v2)
        if numv1 > numv2:
            outNum += numv1
        else:
            outNum += numv2
    return outNum

# HackerRank practice challenge : https://www.hackerrank.com/challenges/non-divisible-subset/problem

setOut = nonDivisibleSubset(3,[1,7,2,4])
print(setOut)
