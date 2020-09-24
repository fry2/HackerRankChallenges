def extraLongFactorials(n):
    multVals = list(range(1, n+1))
    outVal = 1
    for val in multVals:
        outVal *= val
    return outVal

# HackerRank practice challenge : https://www.hackerrank.com/challenges/extra-long-factorials/problem

fact = extraLongFactorials(5)
print(fact)