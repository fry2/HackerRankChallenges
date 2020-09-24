import math


def repeatedString(s, n):
    outVal = s.count('a')*math.floor(n/len(s))+s[:n%len(s)].count('a')
    print(outVal)
    return outVal

# HackerRank practice challenge : https://www.hackerrank.com/challenges/repeated-string/problem

repeatedString('aba',10)