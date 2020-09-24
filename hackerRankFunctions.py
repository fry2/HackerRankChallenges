import math
import numpy as np



def biggerIsGreater(w):
    numW = [ord(letter)-96 for letter in w]
    numW = numW[::-1]
    numI = -1
    flag = 0
    dists = list()
    maxDists = 10000
    while flag == 0:
        numI += 1
        if numI >= len(numW)-1:
            return str('no answer')
        if len(dists) == maxDists:
            numI = dists.index(min(dists))
            flag = 1
            break
        for num2 in numW[numI+1:]:
            if numW[numI] > num2:
                if numI == 0:
                    maxDists = (numW.index(num2)-numI-1)
                dists.append(numW.index(num2)-numI)
                break
            elif numW[numI] == num2:
                break
        #temp = [i for i in numW[numI:] if i < numW[numI]]
    for numI2 in range(numI+1, len(numW)+1):
        if numW[numI2] < numW[numI]:
            num2move = numW.pop(numI)
            numW.insert(numI2, num2move)
            break
    numW[:numI2] = sorted(numW[:numI2], reverse=True)
    numW = numW[::-1]
    numW = ''.join([chr(i + 96) for i in numW])
    return numW











def minimumBribes(q):
    bribes = 0
    for ii in range(len(q)):
        if q[ii] > ii+1:
            if q[ii] - ii > 3:
                outVal = 'Too chaotic'
                print(outVal)
                return
            else:
                bribes += q[ii]-ii-1
    print(bribes)


def minimumSwaps(arr):
    counter = 0
    maxCount = 100
    sArr = sorted(arr)
    while not(arr == sArr) and counter < maxCount:
        backcount = 0
        for ii in range(len(arr)-1, -1, -1):
            if arr[ii] == sArr[ii]:
                backcount += 1
            else:
                break
        dists = []
        for r1 in range(len(arr[:len(arr)-backcount])):
            temp = list()
            for r2 in range(len(sArr)):
                if arr[r1] == sArr[r2]:
                      temp.append(r2-r1)
            dists.append(min(temp,key=abs))
        #dists = [num-i-1 for i, num in enumerate(arr[:len(arr)-backcount])]
        if max(dists) == 1 and min(dists) == -1:
            ind1 = dists.index(1)
            ind2 = dists.index(-1)
        else:
            if dists.count(max(dists)) > 1:
                ind1 = min([i for i, num in enumerate(dists) if num == max(dists)])
            else:
                ind1 = dists.index(max(dists))
            if dists.count(min(dists)) > 1:
                ind2 = max([i for i, num in enumerate(dists) if num == min(dists)])
            else:
                ind2 = dists.index(min(dists))
        temp = arr[ind1]
        arr[ind1] = arr[ind2]
        arr[ind2] = temp
        if counter == maxCount - 1:
            print('Exited because of maxCount')
            return
        counter += 1
    print(counter)
    return counter


inDat = open('input/input01.txt', 'r').read().rstrip().split()
outDat = open('output/output01.txt', 'r').read().rstrip().split()

tNums = [0,1,2,8]
for ii in tNums:
    inDat = open('input/input0'+str(ii)+'.txt', 'r').read().rstrip().split()
    outDat = open('output/output0'+str(ii)+'.txt', 'r').read().rstrip().split()
    arr = [int(i) for i in inDat]
    outArr = minimumSwaps(arr)
    print(int(outDat[0])==outArr, int(outDat[0]))