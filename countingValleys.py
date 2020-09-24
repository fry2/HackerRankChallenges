def countingValleys(n, s):
    level = 0
    valCount = 0
    for mover in s:
        if mover == 'U':
            level += 1
        elif mover == 'D':
            level -= 1
        if level == 0:
            if mover == 'U':
                valCount += 1
    return valCount

# HackerRank practice challenge : https://www.hackerrank.com/challenges/counting-valleys/problem

numValleys = countingValleys(8,'UDDDUDUU')
print(numValleys)